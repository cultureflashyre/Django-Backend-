from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Corporate_signup
from .serializers import CorporateSerializer
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def signup_corporate(request):
    serializer = CorporateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "The data has been received",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# New login view
@api_view(['POST'])
def login_corporate(request):
    # Extract email and password from request data
    email = request.data.get('email')
    password = request.data.get('password')
    
    # Check if email and password are provided
    if not email or not password:
        return Response(
            {"error": "Email and password are required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        # Retrieve the user with the given email
        user = Corporate_signup.objects.get(email=email)
    except Corporate_signup.DoesNotExist:
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    # Verify the provided password against the stored hashed password
    if check_password(password, user.password):
        # Serialize user data (excluding password)
        serializer = CorporateSerializer(user)
        return Response(
            {
                "message": "Login successful",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )