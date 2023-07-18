from rest_framework.permissions import BasePermission


class AnonymousUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (not request.user.is_anonymous)
            and (request.user.role == "ADMIN" or request.user.role == "REGULAR")
        )
