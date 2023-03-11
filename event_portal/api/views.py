from datetime import datetime 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

 

from ..models import *
from .serializers import *
from .renderers import CustomRenderer
from .permissions import *
from .pagination import CustomPagination
from .filters import EventFilter


class CategoryListView(ListAPIView):
    '''
        API endpoint to get list of all category instances
    '''
    serializer_class = CategorySerializer
    renderer_classes = [CustomRenderer]
    queryset = Category.objects.all()
    
class CategoryCreateView(CreateAPIView):
    '''
        API endpoint to create a category instance.
        Only Admins are allowed this endpoint
    '''
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    renderer_classes = [CustomRenderer]
    serializer_class = CategorySerializer
    

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    '''
        API endpoint to retrieve, update or partial update 
        and delete a category instance. Only Admins can perform 
        PUT, PARTIAL PUT and DELETE on any instance
    '''
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    renderer_classes = [CustomRenderer]
    
    def get_object(self):
        slug = self.kwargs["slug"]
        obj = get_object_or_404(Category, slug=slug)  
        return obj 
    
class CreateEventView(CreateAPIView):
    '''
        API endpoint to create an event instance,
        Only users with event_host=True and have HostProfile Instances
        are allowed to access this endpoint
    '''
    serializer_class = EventSerializer 
    permission_classes = [IsAuthenticated, EventHostPermissions]
    authentication_classes = [JWTAuthentication]
    renderer_classes = [CustomRenderer]
     
    def perform_create(self, serializer):
        user = self.request.user 
        serializer.save(host=user)
        
    
class EventListView(ListAPIView):
    '''
        API endpoint to get a list of all event instances
    '''
    serializer_class = EventSerializer 
    pagination_class = CustomPagination
    renderer_classes = [CustomRenderer]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = EventFilter
    search_fields = ["location", "category__name", "title"]
    ordering_fields = ["event_start_date", "date_posted", "last_updated"]
    
    def get_queryset(self):
        return Event.objects.filter(event_start_date__gte=datetime.today().date().strftime('%Y-%m-%d')).order_by("-last_updated")
    
class EventDetailView(RetrieveUpdateDestroyAPIView):
    '''
        API endpoint to retrive, update or partial update 
        and delete an event instance. Only the user who created 
        the instance can perform PUT, PARTIAL PUT and DELETE on any instance
    '''
    serializer_class = EventSerializer 
    renderer_classes = [CustomRenderer]
    authentication_classes = [JWTAuthentication] 
    permission_classes = [EventHostORReadOnly]
    
    
    def get_object(self):
        slug = self.kwargs["slug"]
        obj = get_object_or_404(Event, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj
    
    
class CategoryEventView(ListAPIView):
    '''
        API endpoint to get list of all events by 
        category. The category___slug is passed as 
        a param to get the events list.
    '''
    serializer_class = EventSerializer 
    pagination_class = CustomPagination
    renderer_classes = [CustomRenderer]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ["event_start_date", "date_posted", "last_updated"]
    search_fields = ["location", "title"]
    
    def get_queryset(self):
        slug = self.kwargs["slug"]
        queryset = Event.objects.filter(category__slug=slug)
        return queryset
    
    
    
    
    
    


         

        
        

    
    
    
    
        
    

