from django.db import models

class Category(models.Model): 
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = "categories"

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "products"

class PriceHistory(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "products_price_history"






