from celery import shared_task
from django.core.cache import cache
from .models import Product



# @shared_task
# def add(x,y):
#     return x+y