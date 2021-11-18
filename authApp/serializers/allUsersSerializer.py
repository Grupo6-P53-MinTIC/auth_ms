from rest_framework import serializers
from authApp.models.user import User

class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name']

  