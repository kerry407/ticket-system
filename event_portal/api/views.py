from datetime import datetime 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import viewsets
from django_auto_prefetching import AutoPrefetchViewSetMixin

 

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
    pagination_class = CustomPagination
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
        
        
class EventAPIViewset(AutoPrefetchViewSetMixin, viewsets.ModelViewSet):
    '''
        API endpoint to create, retrieve, update or partial update 
        and delete event(s).
    '''
    serializer_class = EventSerializer 
    pagination_class = CustomPagination
    renderer_classes = [CustomRenderer]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = EventFilter
    search_fields = ["location", "category__name", "title"]
    ordering_fields = ["event_start_date", "date_posted", "last_updated"]
    
    def perform_create(self, serializer):
        user = self.request.user 
        serializer.save(host=user)
    
    def get_queryset(self):
        return Event.objects.filter(
                                event_start_date__gte=datetime.today().date().strftime('%Y-%m-%d')
                                ).order_by("-last_updated")
        
    def get_object(self):
        # read event instance by slug parameter
        slug = self.kwargs["slug"]
        obj = get_object_or_404(Event, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj
        
    def get_permissions(self):
        # define permissions based on the action a user wants to perform
        
        if self.action == 'create':
            self.permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [EventHostOrReadOnly]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()   
    
    
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
    
    
    
    
    
    


         

        
        

    
    
    
    
        
    

