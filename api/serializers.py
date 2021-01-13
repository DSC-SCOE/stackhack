from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username','password1', 'password2',) 