from authApp.models import Car
from authApp.serializers import CarSerializer
from rest_framework import generics

class AllCarsView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

#Retrieve Update and Delete
class CarRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDriverView(generics.ListAPIView):
    serializer_class = CarSerializer
    def get_queryset(self):
        id = self.kwargs['idDriver']
        return Car.objects.filter(userFK_id=id)
