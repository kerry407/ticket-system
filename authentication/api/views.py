from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.validators import ValidationError

from .serializers import AccountSerializer, HostUserProfileSerializer
from event_portal.api.renderers import CustomRenderer
from django.contrib.auth import get_user_model
from ..models import CustomUser, HostUserProfile

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
    serializer_class = HostUserProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [CustomRenderer]
    
    def perform_create(self, serializer):
        instance = self.request.user
        user = get_user_model().objects.get(email=instance.email)
        host = HostUserProfile.objects.filter(user=user)
        if host.exists():
            raise ValidationError(
                                    {
                                        "detail": "This user already has an event host profile"
                                    }
                                )
        serializer.save(user=instance)
        user.event_hoster = True 
        user.save()
        print(user.email, user.event_hoster)

