from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'images')  # Customize the fields displayed in the admin panel list view
