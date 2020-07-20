from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .permissions import UpdateOwnProfile, UpdateOwnUser
from .models import UserProfile
from .serializers import UserProfileSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnUser]
    serializer_class = UserSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = UserProfileSerializer
    permission_classes = [UpdateOwnProfile]


class LoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
