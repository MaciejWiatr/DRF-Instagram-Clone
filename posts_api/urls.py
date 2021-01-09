from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

ROUTER = DefaultRouter()
ROUTER.register("posts", PostViewSet)
ROUTER.register("comments", CommentViewSet)
ROUTER.register("likes", LikeViewSet)

app_name = "posts_api"

urlpatterns = [
    path("feed/", FeedApiView.as_view()),
    path("liked/", LikedApiView.as_view()),
    path("posts/<post_id>/likes", PostLikes.as_view()),
    path("posts/<post_id>/comments", PostComments.as_view()),
    path("", include(ROUTER.urls)),
]
