
from django.utils.translation import gettext as _
from django.core.mail import send_mail

from app_user.models import CustomUser
from config.celery import app



@app.task(bind=True)
def add(x, y):
    return x + y














def send_verification_email(email, verification_code):
    subject = 'Verification Code'
    message = f'Your verification code is: {verification_code}'
    sender_email = 'kubanuch03@gmail.com'
    recipient_email = email
    
    

    try:
        user_obj = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        user_obj = CustomUser.objects.create(email=email)

    user_obj.code = verification_code
    user_obj.save()
    send_mail(subject, message, sender_email, [email], fail_silently=False)

