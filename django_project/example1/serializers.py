import re
from rest_framework import serializers
from .models import User
from django_project.enums import RequestEnum
from django_project.constants import EMAIL_REGEX, USERNAME_REGEX
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['user_type'] = user.user_type

        return token

class UserSerializer(serializers.ModelSerializer):
    signup = serializers.BooleanField(write_only=True,required=False)
    class Meta:
        model = User
        fields =  ['username', 'email','password', 'first_name', 'last_name', 'date_joined', 'signup','user_type','id']
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate_email(self, value): # field level validation
        if not re.fullmatch(EMAIL_REGEX,value):
            raise serializers.ValidationError('Email address is invalid')
        return value
        
    def validate(self, attrs):    # Object level validation
        request = self.context.get('request')
        if request and request.method == RequestEnum.PATCH:
            if 'password' in attrs:
                raise serializers.ValidationError({"password": "Password update is not allowed."})
        if not re.match(USERNAME_REGEX,attrs['username']): 
            raise serializers.ValidationError("Username must start with capital letter and contain at least one special character and two digist's")
        return attrs
    def create(self, validated_data):
        signup = validated_data.pop('signup', False)
        return User.objects.create_user(signup=signup, **validated_data)
 
 

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    user_type = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        # Generate JWT tokens
        # refresh = RefreshToken.for_user(user)
        refresh = CustomTokenObtainPairSerializer.get_token(user)
        access = refresh.access_token

        return {
            "access": str(access),
            "refresh": str(refresh),
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_type": user.user_type,
        }       