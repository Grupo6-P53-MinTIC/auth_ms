from rest_framework import generics

from authApp.models.user import User
from authApp.serializers.allUsersSerializer import AllUsersSerializer

class UserAllView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AllUsersSerializer
    
