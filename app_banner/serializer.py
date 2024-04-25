from rest_framework import serializers
from  .models import Banner


class BannerCRUDserializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ["id", "name", "images"]