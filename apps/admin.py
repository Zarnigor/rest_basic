from django.contrib import admin
from apps.models import Product, Category, Image


# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 1
    min = 1
    max = 3

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass