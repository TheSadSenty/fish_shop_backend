from rest_framework import serializers
from .models import Cart
from products.serializers import ProductsSerializer


class CartSerializer(serializers.ModelSerializer):
    item = ProductsSerializer()

    class Meta:
        model = Cart
        fields = '__all__'
