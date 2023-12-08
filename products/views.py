from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from products.models import Category, Products
from products.serializers import ProductsSerializer, CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
