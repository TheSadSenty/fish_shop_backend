from rest_framework import serializers
from products.models import Category, Products, Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    discount = DiscountSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'discount']


class ProductsSerializer(serializers.ModelSerializer):
    discount = DiscountSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'photo',
                  'price', 'category', 'amount', 'discount']
