from django.core.cache import cache

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from django.utils import timezone
from datetime import timedelta

from .models import CustomUser
from .serializers import UserSerializer, LoginUserSerializer, VerifyUserCodeSerializer,SendCodeSerializer,ForgetPasswordSerializer
from .services import *
from .tasks import send_verification_email
import time


class LoginUserView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        if email and password:

            user = authenticate(username=email, password=password)

            if user:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                data = {
                    "user_id": user.id,
                    "is_staff": user.is_staff,
                    "is_active": user.is_active,
                    "email": user.email,
                    "username": user.username,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "detail": "Authentication failed. User not found or credentials are incorrect."
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"detail": "Invalid input. Both email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )







class RegisterUserView(CreateUserApiView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserVerifyRegisterCode(generics.UpdateAPIView):
    serializer_class = VerifyUserCodeSerializer

    http_method_names = ['patch',]
    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        return CheckCode.check_code(code=code)



#отправить код на почту       
class ForgetPasswordSendCodeView(generics.UpdateAPIView):
    serializer_class = SendCodeSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if not email:
            return Response({"required": "email"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
            # Если пользователь уже существует, просто обновите его код подтверждения и отправьте его
            send_verification_email(email=email)
            return Response({"success":"Код был отправлен на почту"}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            # Если пользователь не существует, создайте нового пользователя и отправьте ему код подтверждения
            user = CustomUser.objects.create(email=email)
            send_verification_email(email=email)
            return Response({"success":"Код был отправлен на почту"}, status=status.HTTP_201_CREATED)
        


# если user забыл пароль при входе
class ForgetPasswordView(generics.UpdateAPIView):
    serializer_class = ForgetPasswordSerializer

    http_method_names = ['patch',]
    def update(self, request, *args, **kwargs):
        
        result = ChangePasswordOnReset.change_password_on_reset(self=self,request=request)

        if result == "success":
            return Response({"success ":"Пароль успешно изменен"}, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(is_superuser=False)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]



class UserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]



