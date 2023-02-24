from datetime import datetime 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework import status 

from ..models import *
from .serializers import *
from .renderers import CustomRenderer

class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    renderer_classes = [CustomRenderer]
    queryset = Category.objects.all()
    
class CategoryCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    renderer_classes = [CustomRenderer]
    serializer_class = CategorySerializer
    

class CategoryDetailView(DestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    renderer_classes = [CustomRenderer]
    
    def get_object(self):
        slug = self.kwargs["slug"]
        obj = get_object_or_404(Category, slug=slug)  
        return obj 
    
class CreateEventView(CreateAPIView):
    serializer_class = EventSerializer 
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    renderer_classes = [CustomRenderer]
     
    def perform_create(self, serializer):
        user = self.request.user 
        serializer.save(host=user)
            
        
class EventDetailView(RetrieveAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    renderer_classes = [CustomRenderer]
    
    def get_object(self):
        slug = self.kwargs["slug"]
        obj = get_object_or_404(Event, slug=slug)
        return obj  
         

        
        

    
    
    
    
        
    

