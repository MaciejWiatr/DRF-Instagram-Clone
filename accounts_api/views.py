from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .permissions import UpdateOwnProfile, UpdateOwnUser
from .models import UserProfile
from .serializers import UserProfileSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnUser]
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["username"]
    search_fields = ["username"]


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = UserProfileSerializer
    permission_classes = [UpdateOwnProfile]


class LoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        user_json = UserSerializer(user).data

        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user": user_json,
            }
        )
