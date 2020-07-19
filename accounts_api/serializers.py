from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    profile_id = serializers.PrimaryKeyRelatedField(
        read_only=True, source="profile")

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "profile_id"]

        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"}
            }
        }


class FollowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id"]


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    follows = serializers.PrimaryKeyRelatedField(
        many=True, queryset=UserProfile.objects.all())
    followed_by = serializers.PrimaryKeyRelatedField(
        many=True, queryset=UserProfile.objects.all())

    class Meta:
        model = UserProfile
        fields = ["id", "user", "age", "photo",
                  "description", "follows", "followed_by"]
