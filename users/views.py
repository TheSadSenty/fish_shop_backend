from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import models, authenticate
from .serializers import UserSerializer, UserLoginSerializer, UserInformathionSerializer, FavoriteProductListSerializer, FavoriteProductCreateUpdateSerializer
from .models import FavoriteProduct
from products.models import Products


class UserViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication]

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(status=status.HTTP_200_OK)
            user = models.User.objects.get(
                username=serializer.data["username"])
            token = Token.objects.create(user=user)
            response["Auth-Token"] = f'{token.key}'
            return response
        try:
            user = models.User.objects.filter(
                username=request.data["username"])
            if user:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "User already exists"})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request, username=serializer.data["username"], password=serializer.data["password"])
            if user is not None:
                try:
                    token = Token.objects.get(user=user)
                except ObjectDoesNotExist:
                    response = Response(status=status.HTTP_200_OK)
                    token = Token.objects.create(user=user)
                    response["Auth-Token"] = f'{token.key}'
                    return response
                response = Response(status=status.HTTP_200_OK)
                response["Auth-Token"] = f'{token.key}'
                return response
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['delete'])
    def logout(self, request):
        if isinstance(request.user, models.User):
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)


class UserInformathionViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = request.user
        serializer = UserInformathionSerializer(queryset)
        return Response(serializer.data)


class FavoriteProductAPIView(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = FavoriteProduct.objects.filter(user=request.user)
        serializer = FavoriteProductListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FavoriteProductCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            product = Products.objects.get(id=serializer.data["product"])
            check_duplicate = FavoriteProduct.objects.filter(product=product)
            if not check_duplicate:
                favorite = FavoriteProduct(product=product, user=request.user)
                favorite.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "Product already in favorite"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "Missing product or product has invalid value"})

    def delete(self, request):
        serializer = FavoriteProductCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            product = Products.objects.get(id=serializer.data["product"])
            check_duplicate = FavoriteProduct.objects.filter(product=product)
            if check_duplicate:
                favorite = check_duplicate[0]
                favorite.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "Product not in favorite"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': "Missing product or product has invalid value"})
