from rest_framework import serializers
from .models import Cart
from products.models import Category, Products

class CartSerializer(serializers.ModelSerializer):
    item_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()  # добавлено

    class Meta:
        model = Cart
        fields = ['item', 'item_name', 'quantity', 'created_at', 'updated_at', 'category_name']

    def get_item_name(self, obj):
        return obj.item.name

    def get_category_name(self, obj):  # добавлено
        return obj.category.name