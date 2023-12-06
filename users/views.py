from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth import models, login, authenticate, logout
from .serializers import UserSerializer, UserLoginSerializer, UserInformathionSerializer, FavoriteProductListSerializer, FavoriteProductCreateUpdateSerializer, UserReviewListSerializer
from .models import FavoriteProduct, UserReview
from products.models import Products


class UserViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    authentication_classes = [SessionAuthentication]

    @method_decorator(csrf_protect)
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        try:
            user = models.User.objects.filter(
                username=request.data["username"])
            if user:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "User already exists"})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    @method_decorator(ensure_csrf_cookie)
    def get_csrf_token(self, request):
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    @method_decorator(csrf_protect)
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request, username=serializer.data["username"], password=serializer.data["password"])
            if user is not None:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

    @method_decorator(csrf_protect)
    @action(detail=False, methods=['delete'])
    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserInformathionViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = request.user
        serializer = UserInformathionSerializer(queryset)
        return Response(serializer.data)


class FavoriteProductAPIView(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = FavoriteProduct.objects.filter(user=request.user)
        serializer = FavoriteProductListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FavoriteProductCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            product = Products.objects.get(id=serializer.data["product"])
            check_duplicate = FavoriteProduct.objects.filter(product=product)
            print(check_duplicate)
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


class UserReviewListViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = UserReview.objects.all()
    serializer_class = UserReviewListSerializer
