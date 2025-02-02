from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, User
from .serializers import UserSerializer
# Create your views here.

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
    