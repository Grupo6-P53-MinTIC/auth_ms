from rest_framework import serializers
from authApp.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def validate (self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        return attrs
    def create (self, validated_data):
        return User.objects.create_user(**validated_data)
        