from firebaseauth.authentication import FirebaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from firebaseauth.permissions import StaffPermission
from firebaseauth.authserializers import CurrentUserSerializer
from django.contrib.auth.models import User

class Register(viewsets.ViewSet):
    
    queryset = User.objects.all()
    
    def list(self, request):
        data = CurrentUserSerializer(self.queryset, many=True)
        return Response(data.data)
    
    def create(self, request):
        
        user = CurrentUserSerializer(data=request.data)
        
        if user.is_valid():
            user.save()
        else:
            return Response(user.errors)   
         
        return Response(user.data)
        
    
