# accounts/views.py

import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CollegeUserSerializer, LoginSerializer

# Set up logger
logger = logging.getLogger('accounts')

class SignupView(APIView):
    def post(self, request):
        logger.debug("Received signup request with data: %s", request.data)
        serializer = CollegeUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("User created successfully with email: %s", request.data.get('email'))
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        else:
            logger.error("Signup failed with errors: %s", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        logger.debug("Received login request with data: %s", request.data)
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            logger.info("User logged in successfully with email: %s", request.data.get('email'))
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            logger.error("Login failed with errors: %s", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)