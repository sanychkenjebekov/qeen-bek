from django.db import models

from app_user.models import CustomUser
from app_product.models import Product




class Favorite(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.product.title}"

    class Meta:
        verbose_name = "Favorites"
        verbose_name_plural = "Favorite"
