from django.urls import path
from app_user.views import *


app_name = "users"
urlpatterns = [
    path("list/user/", UserListView.as_view(), name="list_user"),
    path("delete/user/<int:pk>/", UserDeleteView.as_view(), name="delete_user"),
    

    path("register/user/", RegisterUserView.as_view(), name="register_user"),
    path("login/user/", LoginUserView.as_view(), name="login_user"),

    path('send-code-to-email/', ForgetPasswordSendCodeView.as_view(), name='send_password_reset_code'),
    path('verify/register-code/', UserVerifyRegisterCode.as_view(), name='verify_user_code'),
]
