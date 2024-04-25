from django.db import models
from app_product.models import Product



class NewCollection(models.Model):
    product = models.ManyToManyField(Product)
 



class Recommendations(models.Model):
    product = models.ManyToManyField(Product)