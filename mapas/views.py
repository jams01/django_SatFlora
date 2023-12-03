from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from firebaseauth.permissions import StaffPermission
from firebaseauth.authentication import FirebaseAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .projectserializers import ProjectSerializer

class ProjectCreate(viewsets.ViewSet):
    """
    class used to delete created users

    Attributes:
        authentication_classes: This is the class used to perform the authetication
        permission_classes: This is the class for check if the user have the rights to use this view.
    """
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated, StaffPermission]

    def create(self, request, *args, **kwargs):
        """
        This method creates a new project:
        first validating that data in the creation is correct
        the project is saved
        a response is returned. 
        """
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)