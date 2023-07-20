from rest_framework import serializers
from django.contrib.auth.models import User
from firebaseauth.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("telefono", "direccion", "foto", "nacimiento","sexo")

class CurrentUserSerializer(serializers.ModelSerializer):
    """
        user serialize

        This class takes an user Object and select the filed to be serialized before sending it to the front end.
        
        Attributes:
            profile: an instance of the Profile serializer.
    """
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'first_name', 'last_name', 'profile')