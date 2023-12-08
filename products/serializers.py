from rest_framework import serializers
from products.models import Category, Products


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class ProductsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'photo',
                  'price', 'category', 'amount']
