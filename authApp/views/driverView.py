from rest_framework import generics
from rest_framework.response import Response
from rest_framework import views, status

from authApp.models import User, Car
from authApp.serializers import UserDriverSerializer, UserSerializer, CarSerializer

class AllDriversView(generics.ListAPIView):
    queryset = User.objects.filter(typeAccount='D') 
    serializer_class = UserSerializer