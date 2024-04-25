from decouple import config
import random
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.html import strip_tags

from rest_framework import serializers
from .models import CustomUser

from app_favorite.serializers import FavoriteListSerializer
from app_favorite.models import Favorite




class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "username",
            "phone_number",
            "password",
            "password2",
            "is_staff",
            "is_active"
        )


    def validate(self, attrs):
        if attrs['password'].strip() != attrs['password2'].strip():
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs

 
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("email", "password")

class VerifyUserCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['code']

    
    

class ForgetPasswordSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6,write_only=True)
    password = serializers.CharField(max_length=20,write_only=True)
    confirm_password = serializers.CharField(max_length=20,write_only=True)

    class Meta:
        fields = ['password','password2','code']

class SendCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['email']