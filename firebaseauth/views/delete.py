import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebaseauth.authentication import FirebaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from firebaseauth.permissions import StaffPermission
from django.contrib.auth.models import User


class DeleteUser(viewsets.ViewSet):
    """
    class used to delete created users

    Attributes:
        authentication_classes: This is the class used to perform the authetication
        permission_classes: This is the class for check if the user have the rights to use this view.
    """
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated, StaffPermission]

    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        #delete user from firebase
        try:
            auth.delete_user(user.username)
        except auth.UserNotFoundError:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        #delete user from django
        user.delete()   
        return Response({'detail': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)