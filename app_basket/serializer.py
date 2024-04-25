# from rest_framework import serializers

# from app_product.models import Product, Color, Size

# class SizeBasketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Size
#         fields = ["id", "sizes"]


# class ColorBasketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Color
#         fields = ['id','colors']

# class BasketSerializer(serializers.ModelSerializer):
#     color =ColorBasketSerializer(many=True)
#     class Meta:
#         model = Product
#         fields = ["title", 
#                 "price", 
#                 "description", 
#                 "color",
#                 "size",
#                 "discount",
#                 "images1",
#                 "images2",
#                 "images3"
# ]
#     def to_representation(self, instance):
#         data_product = super().to_representation(instance)        
#         data_product['size'] = SizeBasketSerializer(instance.size.all(), many=True).data
#         data_product['color'] = ColorBasketSerializer(instance.color.all(),many=True).data
        
#         return data_product