from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rides

@receiver(post_save, sender=Rides)
def my_model_post_save_handler(sender, instance, created, **kwargs):
    if created:
        # here to add the notification to rider
        pass
    else:
        print(f"An instance of MyModel was updated: {instance}")
