from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from .models import Author, User
from .serializers import UserSerializer, LoginSerializer, UserAuthorSerializer
from .custompermissions import IsAuthenticatedWithRole
from .tasks import your_async_task
# Create your views here.


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)



class createUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        email_exists = User.objects.filter(email=email).exists()
        
        if email_exists:
            return Response({'message':'Email Already Exists'},status=status.HTTP_400_BAD_REQUEST)
        
        serialized_data = UserSerializer(data=request.data)     
              
        if serialized_data.is_valid():
            serialized_data.save()
            # user = User.objects.create(username=username,email=email )
            # user_data = UserSerializer(user)
            
            return Response(status=status.HTTP_201_CREATED, data=serialized_data.data)
        
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class updateUserView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedWithRole]
    
    def get_object(self):
        email = self.kwargs.get('email')
        try:
            if email:
                return User.objects.get(email=email)
            else:
                Response(status=status.HTTP_404_NOT_FOUND, data={'msg': 'Email Required'})
                
        except User.DoesNotExist:
            Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Email not exist'})
        
        return super().get_object()
    def patch(self, request, *args, **kwargs):
        try:
            user = self.get_object()  # overide the method to handle update with email not with pk
        except Http404:
            return  Response(status=status.HTTP_404_NOT_FOUND, data={"error": "User not exists"})
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

################ Author View #################

class AuthorUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticatedWithRole]
    serializer_class = UserAuthorSerializer
    
    def get_object(self):
        # Custom get_object logic if needed
        user_id = self.kwargs.get('user_id')
        if not user_id:
            raise NotFound(detail="User ID not provided.")
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFound(detail="User not found.")
        
    
    def patch(self, request, *args, **kwargs):
        # Retrieve the object first.
        instance = self.get_object()
        
        # Instantiate the serializer with partial=True
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        # Update the instance (this calls your custom update() method in the serializer)
        self.perform_update(serializer)
        
        # Return a response with the updated data.
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    
############# Celery Testing API ##############
    
    
class CeleryTesting(APIView):
    
    def get(self, request):
        task_result = your_async_task.delay(10, 20)
        return Response(status=status.HTTP_200_OK, data={'data':"hello"})
