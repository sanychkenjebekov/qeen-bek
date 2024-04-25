from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.core.validators import RegexValidator
# from app_favorite.models import Favorite
from .managers import UserManager

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    
    code = models.CharField(max_length=6, blank=True)

    favorites = models.ManyToManyField("app_favorite.Favorite")

    phone_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(r"^\+996\d{9}$")],
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    token_auth = models.CharField(max_length=64, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'User'
        indexes = [
            models.Index(fields=['email']), 
            models.Index(fields=['username']),  
            models.Index(fields=['id']),  
        ]
    
    
    
   