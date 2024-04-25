from django.contrib import admin
from app_user.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email','username','id']

    def get_queryset(self, request):
        return CustomUser.objects.filter(is_superuser=False)
admin.site.register(CustomUser,CustomUserAdmin)