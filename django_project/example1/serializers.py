import re
from rest_framework import serializers
from .models import User
from django_project.enums import RequestEnum



class UserSerializer(serializers.ModelSerializer):
    signup = serializers.BooleanField(write_only=True,required=False)
    class Meta:
        model = User
        fields =  ['username', 'email','password', 'first_name', 'last_name', 'date_joined', 'signup']
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate_email(self, value): # field level validation
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(email_regex,value):
            raise serializers.ValidationError('Email address is invalid')
        return value
        
    def validate(self, attrs):    # Object level validation
        request = self.context.get('request')
        username_regex = r"^(?=.*[^A-Za-z0-9])(?=(?:.*\d){2,})[A-Z].*$"
        if request and request.method == RequestEnum.PATCH:
            if 'password' in attrs:
                raise serializers.ValidationError({"password": "Password update is not allowed."})
        if not re.match(username_regex,attrs['username']): 
            raise serializers.ValidationError("Username must start with capital letter and contain at least one special character and two digist's")
        return attrs
    def create(self, validated_data):
        signup = validated_data.pop('signup', False)
        return User.objects.create_user(signup=signup, **validated_data)
        