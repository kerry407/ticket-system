from ..models import *
from rest_framework import serializers 


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class EventSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)
    host = serializers.StringRelatedField()
    slug = serializers.StringRelatedField()
    class Meta:
        model = Event 
        fields = [
                    "title", "event_date", 
                    "event_time", "location", 
                    "address", "date_created", 
                    "last_updated", "tags", 
                    "about", "expired", "host",
                    "slug"
                ]