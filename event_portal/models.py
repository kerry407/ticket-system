from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
import uuid
# Create your models here.


class BaseTrackingModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True 

class Category(BaseTrackingModel):
    
    EVENT_CATEGORIES = (
        ("Conferences", "Conferences"),
        ("Trade Shows", "Trade Shows"),
        ("Networking", "Networking"),
        ("WorkShops", "WorkShops"),
        ("Product Launch", "Product Launch"),
        ("Charity", "Charity"),
        ("Music", "Music"),
        ("Concert", "Concert"),
        ("Performing & Visual Arts", "Performing & Visual Arts"),
        ("Food & Drink", "Food & Drink"),
        ("Party", "Party"),
        ("Sports & Fitness", "Sports & Fitness"),
        ("Technology", "Technology"),
        ("Digital", "Digital")
    )
    name = models.CharField(max_length=40, choices=EVENT_CATEGORIES, unique=True)
    slug = models.SlugField(db_index=True, editable=False)
    
    class Meta(BaseTrackingModel.Meta):
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    
class Event(BaseTrackingModel):
    title = models.CharField(max_length=250, unique=True)
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    location = models.CharField(max_length=300)
    address = models.CharField(max_length=100, null=True)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(db_index=True, editable=False)
    category = models.ManyToManyField(Category)
    about = models.TextField(null=True)
    expired = models.BooleanField(default=False)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

class Ticket(BaseTrackingModel):
    ticket_type = models.CharField(max_length=25)
    ticket_price = models.FloatField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ticket_id
    
    
class SocialMedia(BaseTrackingModel):
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.event.title}"
        
