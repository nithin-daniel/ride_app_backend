from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password',)



class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    def create(self, validated_data):
        user = User.objects.create_user(
            user_type=validated_data['user_type'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user

    class Meta:
        model = User
        fields = ('password', 'user_type', 'email',)