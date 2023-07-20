from firebaseauth.authentication import FirebaseAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from firebaseauth.permissions import StaffPermission
from firebaseauth.authserializers import CurrentUserSerializer

# Framewrok APIView
class MyView(APIView):
    authentication_classes = (FirebaseAuthentication, )
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class ProtectedView(APIView):
    authentication_classes = (FirebaseAuthentication, )
    permission_classes = (IsAuthenticated, StaffPermission)
    def post(self, request):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

#Framework viewset
class MyViewSet(viewsets.ViewSet):
    authentication_classes = (FirebaseAuthentication, )
    #permission_classes = (IsAuthenticated,)
    #queryset = Restaurante.objects.all()
    serializer_class = CurrentUserSerializer
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated, ]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, StaffPermission]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
    def list(self, request, id=None):
        # Retrieve all objects from the database
        #queryset = MyData.objects.all()
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, id):
        # Create a new object based on the request data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """def retrieve(self, request, pk=None):
        # Retrieve a single object by primary key (pk)
        try:
            instance = MyData.objects.get(pk=pk)
        except MyData.DoesNotExist:
            return Response({'message': 'Object not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MyDataSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # Update an existing object by primary key (pk)
        try:
            instance = MyData.objects.get(pk=pk)
        except MyData.DoesNotExist:
            return Response({'message': 'Object not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MyDataSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        # Delete an existing object by primary key (pk)
        try:
            instance = MyData.objects.get(pk=pk)
        except MyData.DoesNotExist:
            return Response({'message': 'Object not found.'}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""