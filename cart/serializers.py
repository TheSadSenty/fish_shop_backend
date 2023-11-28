from rest_framework import serializers
from .models import Cart
from products.serializers import ProductsSerializer


class CartSerializer(serializers.ModelSerializer):
    item = ProductsSerializer()

    class Meta:
        model = Cart
        exclude = ['user']


class CreateUpdateCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
