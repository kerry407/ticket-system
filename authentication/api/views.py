from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.validators import ValidationError
from django.db import IntegrityError

from .serializers import AccountSerializer, HostUserProfileSerializer
from event_portal.api.renderers import CustomRenderer
from django.contrib.auth import get_user_model
from ..models import HostUserProfile

class CreateAccountView(CreateAPIView):
    '''
        API endpoint for creating an account, 
        It takes three fields in the payload,
        "email", "password1", "password2" 
    '''
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]
    renderer_classes = [CustomRenderer]
    
        
        
class HostProfileCreateView(CreateAPIView):
    '''
        This API endpoint is to allow users create their events,
        Users must have a HostProfile before they can host events
    '''
    serializer_class = HostUserProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [CustomRenderer]
    
    def perform_create(self, serializer):
        instance = self.request.user
        try:
            serializer.save(user=instance)
        except IntegrityError:
            raise ValidationError(
                                    {
                                        "detail": "This user already has an event host profile"
                                    }
                                )
      
        

