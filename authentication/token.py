from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def create_jwt_pair_for_user(user):
    refresh = RefreshToken.for_user(user)
    refresh["email"] = user.email
    refresh["role"] = user.role
    tokens = {"access": str(refresh.access_token), "refresh": str(refresh)}
    return tokens
