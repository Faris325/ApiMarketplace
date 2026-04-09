
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets

from Products.models import Product
from Products import serializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete','patch']       
