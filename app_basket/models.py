# from django.db import models
# from app_product.models import Product
# from app_user.models import CustomUser




# class Basket(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, through='BasketItem')

#     def __str__(self):
#         return f'{self.user}'

    


# class BasketItem(models.Model):
#     basket = models.ForeignKey(Basket, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, related_name='basket_items', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
    