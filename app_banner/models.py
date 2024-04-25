from django.db import models

class Banner(models.Model):
    name = models.CharField(max_length=250)
    images = models.ImageField(upload_to='banner/')
