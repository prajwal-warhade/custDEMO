from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'cat', 'is_active')  # Fields to display in the admin list view
    list_filter = ('cat', 'is_active')  # Filters displayed on the right side in the admin list view
    search_fields = ('name', 'pdetails')  # Fields to search in the admin interface
admin.site.register(Product,ProductAdmin)