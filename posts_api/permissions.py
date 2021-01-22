from rest_framework import permissions


class UpdateOwn(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author.id == request.user.id
