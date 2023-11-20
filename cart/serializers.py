from rest_framework import serializers
from .models import Cart
# from products.models import Category, Products
from products.serializers import CategorySerializer, ProductsSerializer


class CartSerializer(serializers.ModelSerializer):
    item = ProductsSerializer()
    category = CategorySerializer()

    class Meta:
        model = Cart
        fields = ['item', 'quantity', 'created_at', 'updated_at', 'category']
