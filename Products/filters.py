from django_filters import rest_framework as filters

from Products.models import Product


class ProductFilter(filters.FilterSet):
    price_min = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = filters.NumberFilter(field_name="price", lookup_expr="lte")
    
    category = filters.CharFilter(field_name="category", lookup_expr="exact")

    date_min = filters.DateFilter(field_name="created_at", lookup_expr="gte")
    date_max = filters.DateFilter(field_name="created_at", lookup_expr="lte")

    date = filters.DateFilter(field_name="created_at", lookup_expr="iexact")

    class Meta:
        model = Product
        fields = []