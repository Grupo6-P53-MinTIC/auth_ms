from rest_framework import serializers
from authApp.models import User, Car
from .carSerializer import CarSerializer

# create a normal user (Passenger)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email','name', 'lastName', 'birthDate', 'gender', 'documentNumber', 'phoneNumber', 'typeAccount']

# Create a driver user (Driver + car)
class UserDriverSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email','name', 'lastName', 'birthDate', 'gender', 'documentNumber', 'phoneNumber', 'typeAccount', 'car']

    def create(self, validated_data):
        car_data = validated_data.pop('car')
        user = User.objects.create(**validated_data)
        Car.objects.create(**car_data,userFK=user)
        return user

    def to_representation(self, objUser):
        user = User.objects.get(id=objUser.id)
        car = Car.objects.get(userFK=objUser)
        return {
            'username':user.username,
            'email':user.email,
            'name':user.name,
            'lastName':user.lastName,
            'birthDate': user.birthDate,
            'gender':user.gender,
            'documentNumber': user.documentNumber,
            'phoneNumber': user.phoneNumber,
            'typeAccount':user.typeAccount,
            'car': {
                'licenseNumber': car.licenseNumber,
                "carRegistrationNumber": car.carRegistrationNumber,
                "color": car.color,
                "brand": car.brand,
                'model': car.model,
                "description": car.description,
                "equipament": car.equipament,
            }
        }

# Send info od all users
class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'typeAccount']