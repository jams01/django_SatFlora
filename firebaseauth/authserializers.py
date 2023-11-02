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
    Serializador de usuario actual

    Esta clase toma un objeto de usuario y selecciona los campos que se serializarán antes de enviarlos al front end.

    Atributos:
        profile: Una instancia del serializador de Perfil (ProfileSerializer).
    """
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'id', 'first_name', 'last_name', 'profile')
        extra_kwargs = {'password':{'write_only': True}}
    
    def create(self, validated_data):
        """Crea un nuevo usuario a partir de los datos validados.

        Atributos:
            user: Crea una instancia de usuario con los parametros recibidos dentro del Serializador para crear el usuario mediante la librería de firebase
            profile_data: Extae de los parametros recibidos dentro del Serializador el objeto profile, el cual tiene la referencia del profile creado a ese usuario
            validated_data['username']: Se modifica este parametro del profile para asignarle el UID de firebase
            dj_user: Retorna el usuario recién creado en django con los datos del profile
            return dj_user: 
            Profile.objects.create(user=dj_user, **profile_data): Asigna al usuario retornado el profile que se creó
            
        """
        print("Received Data:", validated_data)
        user = auth.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        profile_data = validated_data.pop('profile')
        
        validated_data['username'] = user.uid
        
        dj_user = User.objects.create_user(**validated_data)
        
        Profile.objects.create(user=dj_user, **profile_data)

        return dj_user 