from rest_framework.permissions import BasePermission


class CorePerms(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (not request.user.is_anonymous)
            and (request.user.role == "REGULAR" or request.user.role == "ADMIN")
        )
