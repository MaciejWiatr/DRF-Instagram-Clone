from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *
from .models import *
from .permissions import UpdateOwn
# Create your views here.


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, UpdateOwn]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, UpdateOwn]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, UpdateOwn]
    serializer_class = LikesSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
