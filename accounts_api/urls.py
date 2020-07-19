from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import UserViewSet, LoginView, UserProfileViewSet
app_name = "accounts_api"
ROUTER = DefaultRouter()
ROUTER.register("users", UserViewSet)
ROUTER.register("profiles", UserProfileViewSet)


urlpatterns = [
    path("", include(ROUTER.urls)),
    path("login/", LoginView.as_view())
]
