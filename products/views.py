from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from products.models import Category, Products
from products.serializers import ProductsSerializer, CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]

    def list(self, request):
        queryset = Products.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Products.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
