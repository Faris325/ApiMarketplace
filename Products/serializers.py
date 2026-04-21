
from Products.models import Product
from Products.models import PriceHistory

from rest_framework import serializers 
  
class ProductSerializer(serializers.ModelSerializer):
	"""Сериализатор"""

	class Meta:
		model = Product
		fields = ("name", "category", "price", "quantity",)

	def create(self, validated_data):
		"""При создании объекта, будет сохраняться его история цены"""

		product = Product.objects.create(**validated_data)
		PriceHistory.objects.create(price=product.price, product=product)

		return product 


	def update(self, instance, validated_data):
		"""При обновлении цены, будет сохраняться история цены"""

		old_price = instance.price

		instance.name = validated_data.get('name', instance.name )
		instance.category = validated_data.get('category', instance.category)
		instance.quantity = validated_data.get('quantity', instance.quantity)
		instance.price = validated_data.get('price', instance.price)

		instance.save()

		if old_price != instance.price:
			PriceHistory.objects.create(price=instance.price, product=instance)
			
		
		return instance
	

class ProductPriceGrowthSerializer(serializers.ModelSerializer):
	"""Сериализатор для ProductViewSet - top_price_growth_products"""
	price_change = serializers.FloatField(read_only=True)

	class Meta:
		model = Product
		fields = ("name", "category", "price", "quantity","price_change",)