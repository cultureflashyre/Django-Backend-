# accounts/serializers.py

from rest_framework import serializers
from .models import CollegeUser
from django.contrib.auth.hashers import make_password, check_password

class CollegeUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CollegeUser
        fields = ['first_name', 'last_name', 'phone_number', 'university_college', 
                  'university_college_id', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match"})
        return data

    def validate_email(self, value):
        if CollegeUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        return CollegeUser.objects.create(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            user = CollegeUser.objects.get(email=email)
            if not check_password(password, user.password):
                raise serializers.ValidationError({"password": "Incorrect password"})
        except CollegeUser.DoesNotExist:
            raise serializers.ValidationError({"email": "User with this email does not exist"})
        
        return data