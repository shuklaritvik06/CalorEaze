from rest_framework.permissions import BasePermission


class AnonymousUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_anonymous is not True \
             or request.user.role == "ADMIN"
