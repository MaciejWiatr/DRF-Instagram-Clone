from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth.models import User
from accounts_api.serializers import UserSerializer, UserProfileSerializer


class AuthorSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "profile"]
        depth = 1

        extra_kwargs = {"profile": {"read_only": True}}


class LikesSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Like
        fields = "__all__"

        extra_kwargs = {"author": {"read_only": True}}


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

        extra_kwargs = {"author": {"read_only": True}}


class PostSerializer(serializers.ModelSerializer):

    likes = LikesSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_amount = serializers.SerializerMethodField("get_likes_amount")
    comments_amount = serializers.SerializerMethodField("get_comments_amount")
    author = AuthorSerializer(read_only=True)
    is_liked = serializers.SerializerMethodField("get_is_liked")

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "description",
            "image",
            "created_date",
            "is_liked",
            "likes",
            "likes_amount",
            "comments",
            "comments_amount",
        ]
        depth = 1
        extra_kwargs = {
            "author": {"read_only": True},
            "is_liked": {"read_only": True},
        }

    @staticmethod
    def get_likes_amount(obj):
        return obj.likes.count()

    @staticmethod
    def get_comments_amount(obj):
        return obj.comments.count()

    def get_is_liked(self, obj):
        user = self.context["request"].user
        if user and not user.is_anonymous:
            return bool(obj.likes.filter(author=user))
        return None


class LikesDetailedSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = "__all__"

        extra_kwargs = {"author": {"read_only": True}}
