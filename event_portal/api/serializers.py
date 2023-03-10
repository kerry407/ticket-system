from ..models import *
from rest_framework import serializers 


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class EventSerializer(serializers.ModelSerializer):
    event_categories = serializers.SerializerMethodField()
    host = serializers.StringRelatedField()
    slug = serializers.StringRelatedField()
    
    def get_event_categories(self, obj):
        categories = obj.category.all()
        category_list = [category.name for category in categories]
        return category_list
            
    
    class Meta:
        model = Event 
        fields = [
                    "title", "event_start_date", 
                    "event_start_time","event_end_date", 
                    "event_end_time", "location", 
                    "address", "date_created", 
                    "last_updated", "event_categories", 
                    "about", "expired", "host",
                    "slug"
                ]