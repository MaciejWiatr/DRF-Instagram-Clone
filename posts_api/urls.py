from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

ROUTER = DefaultRouter()
ROUTER.register("posts", PostViewSet)
ROUTER.register("comments", CommentViewSet)

app_name = "posts_api"

urlpatterns = [
    path("", include(ROUTER.urls)),
    path("likes/", LikesApiView.as_view()),
    path("likes/<pk>/", LikesApiView.as_view())
]
