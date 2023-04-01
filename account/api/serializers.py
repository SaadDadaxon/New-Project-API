from django.contrib.auth.models import User

from ..models import Profile
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ProSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    
    class Meta:
        model = Profile
        fields = ['id', 'user', 'avatar', 'bio']
