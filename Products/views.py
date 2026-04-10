
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from Products.models import Product
from Products import serializers

class CustomPageNumberPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete','patch']       
    pagination_class = CustomPageNumberPaginator

    