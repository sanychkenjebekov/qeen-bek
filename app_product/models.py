from django.db import models
from app_category.models import SubCategory
from django.db import models
from app_user.models import CustomUser

class Color(models.Model):
    colors = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.colors
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),  
            models.Index(fields=['colors']),  
            
        ]

class Size(models.Model):
    sizes = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.sizes
    
    class Meta:
        indexes = [
            models.Index(fields=['id']),  
            models.Index(fields=['sizes']),  
            
        ]
class IsFavorite(models.Model):
    isfavorite = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE )
    favorite = models.ForeignKey("app_favorite.Favorite",on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return f"{str(self.user)}"

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField()
    brand = models.CharField(max_length=255)
    characteristics = models.ManyToManyField('CharacteristikTopik')
    is_any = models.BooleanField(default=False)
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    discount = models.CharField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    is_favorite = models.ManyToManyField(IsFavorite,blank=True)
    images1 = models.ImageField(upload_to="text/", blank=True, null=True)
    images2 = models.ImageField(upload_to="text/", blank=True, null=True)
    images3 = models.ImageField(upload_to="text/", blank=True, null=True)


    class Meta:
        indexes = [
            models.Index(fields=['id']), 
            models.Index(fields=['title']), 
            models.Index(fields=['brand']),  
        ]

class CharacteristikTopik(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    indexes = [
            models.Index(fields=['id']),  
            models.Index(fields=['title']),  
            models.Index(fields=['value']),  
            
        ]


