from rest_framework import serializers
from app_collection.models import NewCollection, Recommendations
from app_product.models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "price", "images1", "images2", "images3"]


class NewCollectionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewCollection
        fields = ["product"]


class NewCollectionListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = NewCollection
        fields = ["products"]

    def get_products(self, obj):
        products_queryset = obj.product.all()
        products_data = ProductSerializer(products_queryset, many=True).data
        return products_data




class RecommendationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = ["product"]


class RecommendationListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Recommendations
        fields = ["products"]

    def get_products(self, obj):
        products_queryset = obj.product.all()
        products_data = ProductSerializer(products_queryset, many=True).data
        return products_data

    