from rest_framework import serializers
from .models import Corporate_signup

class CorporateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporate_signup
        fields = ['first_name', 'last_name','company_name', 'phone_number', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}