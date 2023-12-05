from firebaseauth.authentication import FirebaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from firebaseauth.permissions import StaffPermission
from django.http import JsonResponse
from rest_framework import status



class CreateMaps(viewsets.ViewSet):
    
    authentication_classes = (FirebaseAuthentication, )
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
        return Response("Ingreso exitoso a CreateMaps - post")