from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from .permissions import UpdateOwn
from rest_framework.views import Response
# Create your views here.


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
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


class LikesApiView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = LikesSerializer

    def post(self, request, format=None):
        post_id = request.POST['post']
        post = get_object_or_404(Post, pk=post_id)
        new_like, _ = Like.objects.get_or_create(
            author=request.user, post=post)
        serializer = self.serializer_class(new_like).data
        return Response(data=serializer, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        like = get_object_or_404(Like, pk=pk)
        like.delete()
        return Response(status=status.HTTP_200_OK)
