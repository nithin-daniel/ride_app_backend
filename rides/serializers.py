from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Rides

User = get_user_model()


class RideSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rides
        fields = "__all__"

class RideBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rides
        exclude = ('driver', )
