from accounts_api.models import UserProfile
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework import filters
from rest_framework.views import Response
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from .permissions import UpdateOwn
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class FeedApiView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = PostSerializer

    def get(self, request, pk=None):
        follows = UserProfile.objects.get(user=request.user).follows.all()
        feed_queryset = Post.objects.filter(author__id__in=follows)
        data = self.serializer_class(
            feed_queryset, many=True, context={"request": request}
        ).data

        return Response(data=data)


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["author__id", "description"]
    search_fields = ["description"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, UpdateOwn]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class LikeViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LikesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("author__id",)
    queryset = Like.objects.all()

    def create(self, request, *args, **kwargs):
        post_id = request.data["post"]
        post = get_object_or_404(Post, pk=post_id)
        new_like, _ = Like.objects.get_or_create(author=request.user, post=post)
        serializer = self.serializer_class(new_like).data
        return Response(data=serializer, status=status.HTTP_201_CREATED)
