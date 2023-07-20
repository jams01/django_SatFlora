from rest_framework import serializers
from django.contrib.auth.models import User
from firebaseauth.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("telefono", "direccion", "foto", "nacimiento","sexo")

class CurrentUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'first_name', 'last_name', 'profile')