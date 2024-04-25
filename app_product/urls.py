from django.urls import path
from rest_framework.routers import DefaultRouter

from app_product.views import (
    ListAllProductApiView, 
    CreateProductApiView, 
    ProductDeleteApiView, 
    ProductUpdateApiView, 
    ListOneProducApiView, 
    ProductBySubCategory, 

    ColorApiView, 
    ColorRUDView, 
    SizeApiView, 
    SizeRUDView,

    CharacteristikListView,
    CharacteristikDetailView,
    CharacteristikViewSet,
    IsFavoriteApiView
      )
router = DefaultRouter()
router.register(r"characteristik",CharacteristikViewSet, basename='characteristik')

urlpatterns = [
    path('list/all/product/', ListAllProductApiView.as_view()),
    path('list/one/product/<int:id>/', ListOneProducApiView.as_view()),
    path('create/product/', CreateProductApiView.as_view()),
    path('update/product/<int:id>/', ProductUpdateApiView.as_view()),
    path('delete/product/<int:id>/', ProductDeleteApiView.as_view()),
    path('subcategories/<int:subcategory_id>/products/', ProductBySubCategory.as_view()),

    path('create/list/sizes/', SizeApiView.as_view()),
    path('rud/sizes/<int:id>/', SizeRUDView.as_view()),

    path('create/list/colors/', ColorApiView.as_view()),
    path('rud/colors/<int:id>/', ColorRUDView.as_view()),

    path('list/characteristik/', CharacteristikListView.as_view()),
    path('detail/characteristik/<int:pk>/', CharacteristikDetailView.as_view()),

    path('delete/isfavorite/<int:product>/', IsFavoriteApiView.as_view(),name='delete-is_favorite'),


]+ router.urls