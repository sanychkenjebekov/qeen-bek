from rest_framework import serializers

from .models import Favorite

from app_product.serializer import ProductListSerializer
from app_user.models import CustomUser


class FavoriteListSerializer(serializers.ModelSerializer):
    product_image = serializers.ImageField(source='product.images1', read_only=True) 
    product_title = serializers.CharField(source='product.title', read_only=True) 
    class Meta:
        model = Favorite
        fields = ['id','user','product','product_title','product_image','created_at',]


class UserFavoriteSerializer(serializers.ModelSerializer):
    favorites = FavoriteListSerializer(many=True)
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'username',
            'favorites'

        ]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_id = instance.id
        favorites = Favorite.objects.filter(user_id=user_id)
        if favorites.exists():
            favorites_serializer = FavoriteListSerializer(favorites, many=True)
            data['favorites'] = favorites_serializer.data
        return data