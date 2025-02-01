import re
from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['username', 'email']
        
    def validate_email(self, value): # field level validation
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(email_regex,value):
            raise serializers.ValidationError('Email address is invalid')
        return value
        
    def validate(self, attrs):    # Object level validation
        username_regex = r"^(?=.*[^A-Za-z0-9])(?=(?:.*\d){2,})[A-Z].*$"

        if not re.match(username_regex,attrs['username']): 
            raise serializers.ValidationError("Username must start with capital letter and contain at least one special character and two digist's")
        return attrs
        