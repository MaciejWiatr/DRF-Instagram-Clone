from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

ROUTER = DefaultRouter()
ROUTER.register("posts", PostViewSet)
ROUTER.register("comments", CommentViewSet)
ROUTER.register("likes", LikeViewSet)

app_name = "posts_api"

urlpatterns = [
    path("", include(ROUTER.urls)),
    path("feed/", FeedApiView.as_view()),
    path("liked/", LikedApiView.as_view()),
]
