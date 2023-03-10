from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_start_date", "location", "host")
    list_filter = ("event_start_date", "location", "host")
    
@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("facebook", "instagram", "linkedIn", "twitter")
    list_filter = ("facebook", "instagram", "linkedIn", "twitter")
