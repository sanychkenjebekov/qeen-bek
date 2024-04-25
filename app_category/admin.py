from django.contrib import admin
from app_category.models import Category, SubCategory



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")




@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category")
