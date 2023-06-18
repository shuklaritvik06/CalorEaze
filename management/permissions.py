from rest_framework.permissions import BasePermission


class ManagementPerms(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_anonymous is not True \
            and request.user.role == "MANAGER" or request.user.role == "ADMIN"
