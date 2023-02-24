from ..models import *
from rest_framework import serializers 


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event 
        fields = "__all__"