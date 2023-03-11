from ..models import *
from rest_framework import serializers 


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class EventSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField()
    slug = serializers.StringRelatedField()
    category = serializers.ListSerializer(child=serializers.CharField())
    
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
        if data["event_end_date"] < data["event_start_date"]:
            raise serializers.ValidationError("event_end_date cannot be less than event_start_date")
        return data
        
    def create(self, validated_data):
        category = validated_data.pop('category',[])
        event = super().create(validated_data)
        category_qs = Category.objects.filter(name__in=category)
        event.category.add(*category_qs)
        return event