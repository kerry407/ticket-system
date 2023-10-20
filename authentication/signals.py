from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from authentication.models import HostUserProfile

@receiver(post_save, sender=HostUserProfile)
def update_user_instance(sender, instance, created, **kwargs) -> None:
    if created:
        user = instance.user  
        user.event_hoster = True 
        user.save()