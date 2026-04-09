from django.contrib import admin

from django.contrib import admin
from Products.models import Category
  
@admin.register(Category)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name',)
