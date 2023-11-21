from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import CartSerializer
from products.serializers import ProductsSerializer
from .models import Cart
from products.models import Products, Category
from .serializers import *


class CartViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

    def list(self, request):
        queryset = Cart.objects.all()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateUpdateCartSerializer(data=request.data)
        if serializer.is_valid():
            queryset = Products.objects.all()
            product = get_object_or_404(
                queryset, pk=serializer.data["product_id"])
            cart = Cart(item=product, quantity=serializer.data["quantity"])
            cart.save()
            serializer = CartSerializer(cart)
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "Missing product_id or quantity or one of them has invalid value"})

    def retrieve(self, request, pk=None):
        queryset = Cart.objects.all()
        cart = get_object_or_404(queryset, pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = CreateUpdateCartSerializer(data=request.data)
        if serializer.is_valid():
            queryset_cart = Cart.objects.all()
            queryset_product = Products.objects.all()
            cart = get_object_or_404(queryset_cart, pk=pk)
            product = get_object_or_404(
                queryset_product, pk=serializer.data["product_id"])
            cart.item = product
            cart.quantity = serializer.data["quantity"]
            cart.save(force_update=True)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "Missing product_id or quantity or one of them has invalid value"})

    def destroy(self, request, pk=None):
        queryset = Cart.objects.all()
        cart = get_object_or_404(queryset, pk=pk)
        cart.delete()
        return Response(status=status.HTTP_200_OK)
