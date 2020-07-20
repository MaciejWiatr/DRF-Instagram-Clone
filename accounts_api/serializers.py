from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    follows = serializers.PrimaryKeyRelatedField(
        many=True, queryset=UserProfile.objects.all())
    followed_by = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)
    profile_id = serializers.IntegerField(source="id")

    class Meta:
        model = UserProfile
        fields = ["profile_id", "user", "age", "photo",
                  "description", "follows", "followed_by"]

        extra_kwargs = {
            "followed_by": {
                "read_only": True,
            }
        }


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "profile", "posts"]
        depth = 1

        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"}
            },
            "profile": {
                "read_only": True
            }
        }
