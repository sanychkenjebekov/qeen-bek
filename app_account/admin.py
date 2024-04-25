from django.contrib import admin
from app_account.models import PaymentMethod, History


admin.site.register(PaymentMethod)
admin.site.register(History)
