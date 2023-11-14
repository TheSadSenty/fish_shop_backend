from rest_framework import serializers
from products.models import Category, Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'photo',
                  'price', 'category', 'amount']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
