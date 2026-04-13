
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from django.db.models import Avg, Sum, Max, Min, Count

from Products.models import Product
from Products.models import PriceHistory
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


    @action(detail=True, methods=["get"])
    def average_price(self, request, pk=None):
        prices = (PriceHistory.objects.filter(product_id=pk)
                  .aggregate(total_price= Avg('price')))
        # http://127.0.0.1:8000/api/v1/product/1/average_price/
        return Response(prices)
        
    