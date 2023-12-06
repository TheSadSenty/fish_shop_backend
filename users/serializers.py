from rest_framework import serializers
from django.contrib.auth import models
from django.contrib.auth.hashers import make_password
from .models import FavoriteProduct, UserReview
from products.serializers import ProductsSerializer
from products.models import Products


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):

        user = models.User.objects.create(
            email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], username=validated_data['username'], password=make_password(validated_data['password']))
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserInformathionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email']


class FavoriteProductListSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = FavoriteProduct
        fields = ['product']


class FavoriteProductCreateUpdateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Products.objects.all())

    class Meta:
        model = FavoriteProduct
        fields = ['product']


class UserReviewListSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = UserReview
        fields = ['user_public_name', 'text',
                  'product', 'is_anonymous', 'created_at']
