from django.urls import path
from app_category.views import (CategoryAllListApiView, 
CategoryCreateApiView, CategoryRUDApiView, SubCategoryCreateApiView, SubCategoryAllListApiView,
SubCategoryRUDApiView, CategoryBySubCategory, ListOneCategoryApiView, ListOneSubCategoryApiView)



urlpatterns = [
    path('list/all/category/', CategoryAllListApiView.as_view(), name="список всех категории"),
    path('list/one/category/<int:id>/', ListOneCategoryApiView.as_view(), name="список определено категории по id"),
    path('create/category/', CategoryCreateApiView.as_view(), name="создание категории"),
    path('rud/category/<int:id>/', CategoryRUDApiView.as_view(), name="удаление, изменение, детали"),

    path('list/all/subcategory/', SubCategoryAllListApiView.as_view(), name="список всех категории"),
    path('create/subcategory/', SubCategoryCreateApiView.as_view(), name="создание категории"),
    path('rud/subcategory/<int:id>/', SubCategoryRUDApiView.as_view(), name="удаление, изменение, детали"),
    path('categories/<int:category_id>/subcategory/', CategoryBySubCategory.as_view(), name='подкатегории отпределеной категории'),
    path('list/one/subcategory/<int:id>/', ListOneSubCategoryApiView.as_view(), name="список определено категории по id"),
   
]