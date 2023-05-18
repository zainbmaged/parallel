from itertools import product
from rest_framework import serializers
from storeapp.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title","slug", "Category_id"]



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title","description","category", "discounted_price","selling_price", "id"]
    
    category = Categoryserializer()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "date_created", "name", "description"]
    
    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id = product_id,  **validated_data)

class SimpleProductSerializer(serializers.ModelSerializer):
     class Meta:
     model= Product
     fields=["id","name","price"]


class CartItemSerializer(serializers.ModelSerializer):
     product=ProductSerializer(many=False)
     sub_total=serializers.SerializerMethodField()
     class Meta:
        model= Cartitems
        fields=["id","cart","product","quantity","sub_total"]
    
    def total(self,cartitem:Cartitems):
        return cartitem.quantity * cartitem.product.price

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items=CartItemSerializer(many=True)
    grand_total =serializers.SerializerMethodField(method_name='main_total')
    class Meta:
        model = Cart
        fields = ["id","items","grand_total"]
   
   
    def main_total(self,cart:Cart):
        items = cart.items.all()
        total = sum([item.quantity *item.product.price for item in items])
        return total


