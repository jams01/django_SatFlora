from firebaseauth.authentication import FirebaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from firebaseauth.permissions import StaffPermission
from firebaseauth.authserializers import CurrentUserSerializer
from django.contrib.auth.models import User

class Register(viewsets.ViewSet):
    """Clase orientada al registro de usuarios.

        Atributos:
            queryset = User.objects.all(): Esta línea define un atributo de clase llamado 
            permission_classes: Hace que la clase solo pueda ser accedida por medio del staff
        """
    permission_classes = [StaffPermission];
    queryset = User.objects.all()
    
    def list(self, request):
        data = CurrentUserSerializer(self.queryset, many=True)
        return Response(data.data)
    
    def create(self, request):
        
        """Función encargada de recibir el query donde se albergan los datos del usuario para su respectiva creación.

        Atributos:
            user: Crea una instancia de usuario con los parametros recibidos dentro de su Serializador.
            if user.is_valid(): Esta línea verifica si los datos proporcionados en la solicitud son válidos según las reglas de validación definidas en el CurrentUserSerializer.
            user.save(): Si los datos son válidos, esta línea guarda el nuevo usuario en la base de datos.
            return Response(user.data): Finalmente, se devuelve una respuesta en formato JSON con los datos del usuario creado si la operación fue exitosa.
        """
        try:
            user = CurrentUserSerializer(data=request.data)

            if user.is_valid():
                user.save()
                return Response(user.data)
            else:
                return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Manejo de excepciones generales
            return Response({'message': 'Error al registrar usuario'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        
    
