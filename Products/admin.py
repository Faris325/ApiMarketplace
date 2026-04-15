from django.contrib import admin

from django.contrib import admin
from Products.models import Category
from Products.models import Product

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name','category','quantity','created_at',)


