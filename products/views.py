from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from products.models import Category, Products
from django.http import Http404
from products.serializers import ProductsSerializer, CategorySerializer


class ProductsDetail(APIView):
    def get_object(self, id):
        try:
            return Products.objects.get(id=id)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        product = self.get_object(id)
        serializer = ProductsSerializer(product)
        return JsonResponse(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        product = self.get_object(id)
        serializer = CategorySerializer(product)
        return JsonResponse(serializer.data)
