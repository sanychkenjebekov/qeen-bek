from rest_framework import mixins,generics,status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import gettext as _
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password

from .models import CustomUser
import random
import string
import requests


from .tasks import send_verification_email

def generate_verification_code(length=6):
    """Generate a random verification code."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


# def send_verification_code(email):

#     verification_code = generate_verification_code()

#     subject = 'Verification Code'
#     message = f'Your verification code is: {verification_code}'
#     sender_email = 'kubanuch03@gmail.com'
#     recipient_email = email

#     try:
#         user_obj = CustomUser.objects.get(email=email)
#     except CustomUser.DoesNotExist:
#         user_obj = CustomUser.objects.create(email=email)
#     user_obj.code = verification_code
#     user_obj.save()

#     send_mail(subject, message, sender_email, [recipient_email], fail_silently=False)








def send_code_to_number(email_or_phone):
    login = 'erko'
    password = 'Bishkek2022'
    sender = 'SMSPRO.KG'

    transactionId = generate_verification_code()
    code = generate_verification_code()

    xml_data = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
    <message>
        <login>{login}</login>
        <pwd>{password}</pwd>
        <id>{transactionId}</id>
        <sender>{sender}</sender>
        <text>{code}</text>
        <phones>
            <phone>{email_or_phone}</phone>
        </phones>
    </message>"""


    url = 'https://smspro.nikita.kg/api/message'
    headers = {'Content-Type': 'application/xml'}

    response = requests.post(url, data=xml_data, headers=headers)
    user_obj = CustomUser.objects.get(email_or_phone=email_or_phone)
    user_obj.code = code
    print(user_obj.number)
    user_obj.save()
    if response.status_code == 200:
        print('Ответ сервера:', response.text)



class CreateUserApiView(mixins.CreateModelMixin, generics.GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        verification_code = generate_verification_code()  # Функция генерации кода верификации

        serializer.save()

        if "@" in email:
            send_verification_email(email, verification_code)  # Вызов задачи для отправки сообщения

        return Response({"success": "Код был отправлен на указанный реквизит"}, status=status.HTTP_201_CREATED)

class CheckCode():
        @staticmethod
        def check_code(code):
            try:
                user = CustomUser.objects.get(code=code)
                user.is_active = True
                user.save()
                refresh = RefreshToken.for_user(user=user)
                return Response({
                    'detail': 'Successfully confirmed your code',
                    'user_id': user.id,
                    'is_staff': user.is_staff,
                    'is_active': user.is_active,
                    'phone_number': user.phone_number,
                    'email': user.email,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'refresh_lifetime_days': refresh.lifetime.days,
                    'access_lifetime_days': refresh.access_token.lifetime.days,
                    'message': 'Код успешно обновлен'
                })
            except CustomUser.DoesNotExist:
                return Response({"error":"Пользователь не найден"})



class ChangePasswordOnReset:

    def change_password_on_reset(self,request):
        # user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        new_password = serializer.validated_data.get('password')
        confirm_password = serializer.validated_data.get('confirm_password')

        if new_password != confirm_password:
            return Response({"success":"Пароли не совпадают"}, status=status.HTTP_400_BAD_REQUEST)
        
        check_code_result = CheckCode.check_code(code)
        if 'error' in check_code_result:
            return Response(check_code_result['error'], status=status.HTTP_400_BAD_REQUEST)



        user = CustomUser.objects.get(code=code)
        user.set_password(new_password)
        user.save()
        return {"success":"change password"}



class ChangePassword:
    
    @staticmethod
    def change_password_on_profile(request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_new_password')

        if not check_password(old_password, user.password):
            return Response({"error":"Старый пароль неверный"})
        
        if new_password != confirm_password:
            return Response({"error":"Пароли не совпадают"})

        try:
            user.set_password(new_password)
            user.save()
            return Response({"success":"change password"})
        except Exception as e:
            return str(e)
        
    
    
    def send_email_code(email_or_phone):

        try:
            CustomUser.objects.get(email_or_phone=email_or_phone)
            if "@" in email_or_phone:
                send_verification_code(email_or_phone=email_or_phone)
                return Response({"success":"Код был отправлен на ваш email"})
            elif "996" in email_or_phone:
                send_code_to_number(email_or_phone=int(email_or_phone))
                return Response({"success":"Код был отправлен на ваш номер"})
            else:
                return Response({"success":"The given data invalid"})
        except CustomUser.DoesNotExist:
            return Response({"success":"Пользователь с таким емейлом не существует"})
        


    

