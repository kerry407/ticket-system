from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.views import APIView 

from .serializers import AccountSerializer
from ..models import CustomUser

class CreateAccountView(APIView):
    
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            account_details = serializer.save()
            refresh = RefreshToken.for_user(account_details)
            serialized_data = serializer.data 
            serialized_data["tokens"] = {
                                         "refresh_token": str(refresh),
                                         "access_token": str(refresh.access_token)
                                        }
            return Response(
                            {
                                "status": "Successful",
                                "data": serialized_data
                            },
                            status=status.HTTP_201_CREATED
                           )   
        return Response(
                        {
                            "status": "Error",
                            "data": serializer.errors
                        },
                        status=status.HTTP_400_BAD_REQUEST
                       )

