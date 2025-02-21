from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Corporate_signup
from .serializers import CorporateSerializer

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