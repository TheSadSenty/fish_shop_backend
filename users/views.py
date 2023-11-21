from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth import models
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

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

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
