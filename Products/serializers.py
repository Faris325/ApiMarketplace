
from Products.models import Product
from Products.models import PriceHistory

from rest_framework import serializers 
  
class ProductSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		product = Product.objects.create(**validated_data)
		PriceHistory.objects.create(price= product.price, product=product)

		return product 

	class Meta:
		model = Product
		fields = ("name", "category", "price", "quantity",)


	def update(self, instance, validated_data):

		old_price = instance.price

		instance.name = validated_data.get('name', instance.name )
		instance.category = validated_data.get('category', instance.category)
		instance.quantity = validated_data.get('quantity', instance.quantity)
		instance.price = validated_data.get('price', instance.price)

		instance.save()

		if old_price != instance.price:
			PriceHistory.objects.create(price=instance.price, product=instance)
			
		
		return instance