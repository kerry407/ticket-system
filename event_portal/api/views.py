from datetime import datetime 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
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
from .permissions import EventHostPermission 
from .pagination import CustomPagination
from .filters import EventFilter


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
        
    
class EventListView(ListAPIView):
    serializer_class = EventSerializer 
    pagination_class = CustomPagination
    renderer_classes = [CustomRenderer]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = EventFilter
    search_fields = ["location", "tags__name", "title"]
    ordering_fields = ["event_date", "date_posted", "last_updated"]
    
    def get_queryset(self):
        return Event.objects.filter(event_date__gte=datetime.today().date().strftime('%Y-%m-%d')).order_by("-last_updated")
    
class EventUpdateView(UpdateAPIView):
    serializer_class = EventSerializer 
    renderer_classes = [CustomRenderer]
    authentication_classes = [JWTAuthentication]
    permission_classes = [EventHostPermission]
    
    def get_object(self):
        slug = self.kwargs["slug"]
        obj = get_object_or_404(Event, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj
    
    
class EventDeleteView(DestroyAPIView):
    permission_classes = [EventHostPermission]
    renderer_classes = [CustomRenderer]
    authentication_classes = [JWTAuthentication]
    serializer_class = EventSerializer 
    
    def get_object(self):
        slug = self.kwargs["slug"]
        obj = get_object_or_404(Event, slug=slug)
        self.check_object_permissions(self.request, obj) 
        return obj 
    
    
    
    
    


         

        
        

    
    
    
    
        
    

