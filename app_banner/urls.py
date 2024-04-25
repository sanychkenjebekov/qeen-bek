from django.urls import path
from .views import BannerList, BannerDeleteandREtvew,BannerCreate

urlpatterns = [
    path('banners/', BannerList.as_view(), name='banner-list'),
    path('banners/create/', BannerCreate.as_view(), name='banner-create'),
    path('banners/<int:pk>/', BannerDeleteandREtvew.as_view(), name='banner-detail'),
]