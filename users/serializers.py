from rest_framework import serializers
from django.contrib.auth import models
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):

        user = models.User.objects.create(
            email=validated_data['email'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], username=validated_data['username'], password=make_password(validated_data['password']))
        return user
