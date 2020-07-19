from django.shortcuts import render
from .serializers import UserProfileSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile, UpdateOwnUser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import mixins
from .models import UserProfile


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
