import logging
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Candidate
from .serializers import CandidateSerializer
from django.contrib.auth.hashers import check_password

logger = logging.getLogger(__name__)

@api_view(['POST'])
def signup_candidate(request):
    serializer = CandidateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "The data has been received",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_candidate(request):
    logger.info("Waiting for login data from Angular")
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        candidate = Candidate.objects.get(email=email)
        if check_password(password, candidate.password):
            logger.info(f"Login successful for {email}")
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            logger.warning("Incorrect password")
            return Response({"error": "invalid Email or Password"}, status=status.HTTP_401_UNAUTHORIZED)
    except Candidate.DoesNotExist:
        logger.error("Email not found")
        return Response({"error": "invalid Email or Password"}, status=status.HTTP_404_NOT_FOUND)