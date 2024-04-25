from django.conf import settings
from django.core.mail import send_mail

from app_user.models import CustomUser


def send_verification_mail(email):
    url = f'http://localhost:8000/account/change/password/'
    user = CustomUser.objects.get(email=email)
    user.save()
    subject = 'Ваша ссылка на сброс парля'
    message = f'Ваша ссылка на сброс пароля:\n{url}\nСпасибо за использование нашего приложения.'
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [email])