from datetime import date

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from rest_framework import status
from django.db.models import F
from django.db.models import DecimalField
from django.db.models import ExpressionWrapper 
from django.db.models import OuterRef
from django.db.models import Subquery

from Products.models import Product
from Products.models import PriceHistory
from Products import serializers
from Products.filters import ProductFilter

class CustomPageNumberPaginator(PageNumberPagination):
    """Пагинатор"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    """
    Используется для создания, изменения, добавления, получения, удаления запсей
    """
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete','patch']       
    pagination_class = CustomPageNumberPaginator
    filterset_class = ProductFilter


    @action(detail=True, methods=["get"])
    def average_price(self, request, pk=None):
        """Возврщает среднюю цену товара, возможно указание даты """

        start_str = request.query_params.get("start")
        end_str = request.query_params.get("end")

        qs = PriceHistory.objects.filter(product_id=pk)

        if start_str and end_str:
            try:
                start = date.fromisoformat(start_str)
                end = date.fromisoformat(end_str)
            except ValueError:
                return Response(
                    {"error": "Дата должна быть YYYY-MM-DD"},
                    status=400
                )

            qs = qs.filter(created_at__range=(start, end))

        avg_price = qs.aggregate(avg=Avg("price"))["avg"]

        if avg_price is None:
            return Response({
                "message": "Нет данных",
                "avg_price": None
            })

        return Response({
            "avg_price": round(avg_price, 2)
        })
    
        # http://127.0.0.1:8000/api/v1/product/1/average_price/?start=2024-01-01&end=2024-12-31

    @action(detail=True, methods=["get"])
    def price_change_percentage(self, request, pk=None):
        """Возвращает среднюю цену на товар"""

        try:
            obj = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({"message":"нет такого объекта"},
                            status=status.HTTP_404_NOT_FOUND
                            )
            
        min_obj = PriceHistory.objects.filter(
            product_id=pk
        ).order_by("created_at").first()

        price = ((obj.price - min_obj.price)/min_obj.price)*100

        return Response({
            "price_change": round(price, 2),
            "unit": "%"
        })
            
    @action(detail=False, methods=["get"])
    def top_price_growth_products(self, request):
        """Возваращет 100 товаров с наибольшим изменением цены вверх"""

        last_price = PriceHistory.objects.filter(
            product=OuterRef('pk')  
        ).order_by('-created_at').values('price')[:1]

        second_price = PriceHistory.objects.filter(
            product=OuterRef('pk')  
        ).order_by('created_at').values('price')[:1]

        price = Product.objects.annotate(
                last_price=Subquery(last_price),
                second_price=Subquery(second_price)
            ).annotate(
                price_change=ExpressionWrapper(
                    (F("last_price") - F("second_price")) 
                    * 100 / F("second_price"),
                    output_field=DecimalField()
                )
            ).order_by('-price_change')[:101]

        page = self.paginate_queryset(price)  # Пагинация 
        serializer = serializers.ProductPriceGrowthSerializer(page, many=True)

        return self.get_paginated_response(serializer.data) # Ответ с пагниацией
    


    


        

        
    