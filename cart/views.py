from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CartSerializer
from products.serializers import ProductSerializer
from .models import Cart
from products.models import Products, Category

class CartAPI(APIView):
    def get(self, request, format=None):
        # Получаем ID пользователя из параметра запроса
        # user_id = request.GET.get('user_id')

        try:
            # Получаем корзину по ID пользователя
            cart = Cart.objects.all()
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Cart not found.'})

        # Сериализуем данные корзины
        serializer = CartSerializer(cart, many=True)
        return Response({"data": serializer.data, "cart_total_price": self.calculate_total_price(cart)})

    def post(self, request, **kwargs):
        # Получаем данные из тела запроса
        # product_name = request.data.get('product_name')
        # quantity = request.data.get('quantity', 1)
        # category = request.data.get('category')
        product_name = request.data.get('product_name')
        quantity = request.data.get('quantity', 1)
        category_name = request.data.get('category_name')

        try:
            # Получаем продукт по ID
            product = Products.objects.get(name=product_name)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Product not found.'})

        # # Проверяем существование категории
        # if not Category.objects.filter(name=category_name).exists():
        #     return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Category does not exist.'})

        try:
            # Получаем продукт по ID
            category = Category.objects.get(name=product.category.name)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Category does not exist.'})

        # Создаем или получаем корзину
        cart, created = Cart.objects.get_or_create(item=product, category=category, defaults={'quantity': quantity})
        if not created:
            # Если запись уже существует, обновим quantity
            cart.quantity += int(quantity)
            cart.save()

        return Response({"message": "cart updated"}, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, format=None):
        product_id = request.data.get('product_id')

        if not product_id:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Product ID is required for deletion.'})

        try:
            product = Products.objects.get(pk=product_id)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Product not found.'})

        try:
            cart_item = Cart.objects.get(item=product)
            cart_item.delete()
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Item not found in the cart.'})

        return Response(status=status.HTTP_204_NO_CONTENT)

    def calculate_total_price(self, cart_items):
        # Рассчитываем общую стоимость корзины
        total_price = sum(item.item.price * item.quantity for item in cart_items)
        return total_price