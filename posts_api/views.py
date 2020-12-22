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
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description", "author__username"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, UpdateOwn]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikesApiView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LikesSerializer

    def get(self, request, pk=None):
        if pk:
            like = self.serializer_class(Like.objects.get(id=pk)).data
            return Response(data=like)
        likes = self.serializer_class(Like.objects.all(), many=True).data
        return Response(data=likes)

    def post(self, request, format=None):
        post_id = request.data["post"]
        post = get_object_or_404(Post, pk=post_id)
        new_like, _ = Like.objects.get_or_create(author=request.user, post=post)
        serializer = self.serializer_class(new_like).data
        return Response(data=serializer, status=status.HTTP_201_CREATED)

    def delete(self, request, pk=None):
        if pk:
            like = get_object_or_404(Like, pk=pk)
            if like.author == request.user:
                like.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
