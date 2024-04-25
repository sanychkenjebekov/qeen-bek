from rest_framework import serializers
from app_user.models import CustomUser
from app_account.models import PaymentMethod, History


class ChangeUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'full_name',
            "phone_number",
        )


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "username",
            "password",
            "phone_number",

        )


class HistoryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
        )



class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['text']


class SendResetCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=30)
    confirming_new_password = serializers.CharField(max_length=30)

    class Meta:
        fields = ['new_password', 'confirming_new_password']    


from app_product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "discount", "price",  "images1", "images2", "images3"]




class HistoryListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    user = HistoryUserSerializer()
    class Meta:
        model = History
        fields = ['id', 'products', 'user', 'price', 'lastname', 'firstname', 'types', 'location', 'payment_type', 'status', 'delivery_date']

    

    def get_products(self, obj):
        products_queryset = obj.products.all()
        products_data = ProductSerializer(products_queryset, many=True).data
        return products_data




class HistoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['products', 'user', 'price', 'lastname', 'firstname', 'types', 'location', 'payment_type', 'status', 'delivery_date']