from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import CartSerializer
from .models import Cart
from products.models import Products
from .serializers import *


class CartReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = CreateUpdateCartSerializer(data=request.data)
        if serializer.is_valid():
            queryset = Products.objects.all()
            product = get_object_or_404(
                queryset, pk=serializer.data["product_id"])
            cart = Cart(
                item=product, quantity=serializer.data["quantity"], user=request.user)
            cart.save()
            serializer = CartSerializer(cart)
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "Missing product_id or quantity or one of them has invalid value"})

    def update(self, request, pk=None):
        serializer = CreateUpdateCartSerializer(data=request.data)
        if serializer.is_valid():
            queryset_cart = Cart.objects.filter(user=request.user)
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
        queryset = Cart.objects.filter(user=request.user)
        cart = get_object_or_404(queryset, pk=pk)
        cart.delete()
        return Response(status=status.HTTP_200_OK)
