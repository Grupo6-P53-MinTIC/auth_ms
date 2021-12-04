from rest_framework import generics
from rest_framework.response import Response
from rest_framework import views, status

from authApp.models import User, Car
from authApp.serializers import UserDriverSerializer, UserSerializer, CarSerializer

class AllDriversView(generics.ListAPIView):
    def get(self, request):
        driver = User.objects.filter(typeAccount='D') 
        serialized = UserSerializer(driver, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)