# accounts/views.py
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import CollegeUser
from .serializers import CollegeUserSerializer, LoginSerializer
from django.http import JsonResponse
# Set up logger
logger = logging.getLogger('accounts')

class SignupView(APIView):
    def post(self, request):
        logger.debug("Received signup request with data: %s", request.data)
        serializer = CollegeUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("User created successfully with email: %s", request.data.get('email'))
            # Enhanced response similar to candidate view
            return Response({
                "message": "The data has been received",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            logger.error("Signup failed with errors: %s", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        logger.debug("Received login request with data: %s", request.data)
        
        # Basic email/password validation from candidate view
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            logger.warning("Missing email or password")
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # Try-except block similar to candidate view
            try:
                user = CollegeUser.objects.get(email=email)
                # Note: We won't implement check_password here as we're keeping serializer-based validation
                logger.info("User logged in successfully with email: %s", email)
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            except CollegeUser.DoesNotExist:
                logger.error("Email not found: %s", email)
                return Response({"error": "Invalid Email or Password"}, status=status.HTTP_404_NOT_FOUND)
        else:
            logger.error("Login failed with errors: %s", serializer.errors)
            return Response({"error": "Invalid Email or Password"}, status=status.HTTP_401_UNAUTHORIZED)
def check_phone(request):
    phone = request.GET.get('phone')
    exists = CollegeUser.objects.filter(phone_number=phone).exists()
    return JsonResponse({'exists': exists})

def check_email(request):
    email = request.GET.get('email')
    exists = CollegeUser.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})
