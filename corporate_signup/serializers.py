from rest_framework import serializers
from .models import Corporate_signup
from django.contrib.auth.hashers import make_password

class CorporateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporate_signup
        fields = ['first_name', 'last_name', 'company_name', 'phone_number', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extract the password from validated data and hash it
        password = validated_data.pop('password')
        # Create a new user instance with the remaining data
        user = Corporate_signup(**validated_data)
        # Hash the password and set it on the user instance
        user.password = make_password(password)
        user.save()
        return user