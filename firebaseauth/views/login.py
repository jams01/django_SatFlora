from firebaseauth.authentication import FirebaseAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from firebaseauth.permissions import StaffPermission
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import status

from ..models import Profile, User

import firebase_admin.auth as auth
from django.db import transaction

class MyView(APIView):
    
    """
    An ApiView for managing user instances.

    This is an example on how document the code

    Attributes:
        authentication_classes: This is the class used to perform the authetication
        permission_classes: This is the class for check if the user have the rights to use this view.
    """
    def post(self, request):
        """
            This method is used when something is posted to this path

            This post is open to any logged in user since the permission_class only requires IsAuthenticated

            Args:
            request (Request): The request object, it contains the info of the user logged in and other info.

        Returns:
            Response: The serialized data of the user id and auth status.
        """
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class ProtectedView(APIView):
    """
    A Protected ApiView for managing user instances.

    This is an example on how document the code

    Attributes:
        authentication_classes: This is the class used to perform the authetication
        permission_classes: This is the class for check if the user have the rights to use this view.
    """
    authentication_classes = (FirebaseAuthentication, )
    permission_classes = (IsAuthenticated, StaffPermission)
    def post(self, request):
        """
            This method is used when something is posted to this path

            This post can only be accesed by staff members since uses the StaffPermission class. This class is implementd to 
            check if the user is a staff member

            Args:
            request (Request): The request object, it contains the info of the user logged in and other info.

        Returns:
            Response: The serialized data of the user id and auth status.
        """
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class Login(viewsets.ViewSet):
    
    """
    An ViewSet for managing user instances.

    This is an example on how document the code, and this is the framework we will use, ViewSet

    Attributes:
        authentication_classes: This is the class used to perform the authetication
        serializer_class: This class takes and model object and convert it to a string type to be 
        sent to the front end.
    """
    queryset = User.objects.all()
    
    def post(self, request):
        try:
            firebase_token = request.data.get("firebase_token")
            
            decoded_token = auth.verify_id_token(firebase_token)
        
            uid = decoded_token['uid']
            username = decoded_token.get('email')
            
            return Response({'user_uid': uid,'username':username}, status=status.HTTP_200_OK)
        except:
            # Maneja el error de token de Firebase inválido
            return Response({'message': 'Token de Firebase inválido'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def get_permissions(self):
        """
        This method set up the permission for each view, 
        list view can be accessed for logged in user, but create view can only be accessed for staff.

        Returns:
            A list with the answer for each permission check.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated, ]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, StaffPermission]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    def list(self, request, id=None):
        """
        This method return the info of the user serialized by CurrentUserSerializer, 
        
        Args:
            request: The request object
            id: For know is not used

        Returns:
            A serialized user object
        """
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def getTest(self, request):
        print("Solicitud GET recibida")
        return Response({'message': 'Esta es una vista de prueba.'})    

