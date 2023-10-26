from ..models import *
from rest_framework import serializers 


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class EventSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField()
    slug = serializers.StringRelatedField()
    
    class Meta:
        model = Event 
        fields = [
                    "title", "event_start_date", 
                    "event_start_time","event_end_date", 
                    "event_end_time", "location", 
                    "address", "date_created", "category",
                    "last_updated", "about", "expired", "host",
                    "slug"
                ]
        
    def validate(self, data):
        try:
            if data["event_end_date"] < data["event_start_date"]:
                raise serializers.ValidationError("event_end_date cannot be less than event_start_date")
        except KeyError:
            pass 
        return data
        
    