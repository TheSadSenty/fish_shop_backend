from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from products.models import Category, Products
from products.serializers import ProductsSerializer, CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    pagination_class = PageNumberPagination
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    pagination_class = PageNumberPagination
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
