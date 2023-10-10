from rest_framework import serializers
from django.contrib.auth.models import User
from firebaseauth.models import Profile
import firebase_admin.auth as auth

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("phone", "address", "picture", "birthdate","sex")

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
        fields = ('username', 'email', 'password', 'id', 'first_name', 'last_name', 'profile')
        extra_kwargs = {'password':{'write_only': True}}
    
    def create(self, validated_data):
        
        print("Received Data:", validated_data)
        #Create firebase user
        user = auth.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        # Extract profile data from validated_data
        profile_data = validated_data.pop('profile')
        
        # Modify the username with Firebase UID
        validated_data['username'] = user.uid
        
        # Create user in Django with Firebase UID for 'username'
        dj_user = User.objects.create_user(**validated_data)
        
        # Crea un perfil asociado al usuario de Django
        Profile.objects.create(user=dj_user, **profile_data)

        return dj_user 