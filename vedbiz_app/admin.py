from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude=('category_code',)
    list_display = ['category_code', 'name']

    search_fields = ['category_code']
    list_filter = ['category_code']

    class Meta:
        model = Category
        fields = '__all__'
        list_display = ['category_code', 'name']
        list_filter = ['category_code']
        ordering = ['category_code']
        search_fields = ['category_code']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude=('product_code',)
    list_display = ['product_code', 'name', 'price', 'image']
