from django.db import models
from django.contrib.auth import get_user_model

import uuid
# Create your models here.
User = get_user_model()


class Rides(models.Model):

    RIDE_STATUS = [("ST", "Started"), ("CP", "Completed"), ("CD", "Cancelled")]
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    rider = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="rider")
    driver = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="driver", null=True, blank=True
    )
    pickup_location = models.CharField(max_length=200)
    dropoff_location = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=RIDE_STATUS, default="ST")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
