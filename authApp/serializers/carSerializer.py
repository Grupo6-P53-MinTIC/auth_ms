from rest_framework import serializers
from authApp.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [ 'carRegistrationNumber','licenseNumber','color', 'brand','model','description', 'equipament', 'userFK']
