from rest_framework.generics import GenericAPIView
from .serializer import RegisterSerializer, LoginSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate
from .token import create_jwt_pair_for_user
from rest_framework import status
from pytz import timezone
from datetime import datetime
from .models import DiveUser


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []

    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        data = serialized_data.initial_data
        data["registration_time"] = datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({
                "status": "success",
                "code": 201,
                "message": "User registered successfully",
                "data": serialized_data.data
            }, status=status.HTTP_201_CREATED)
        return JsonResponse({"error": {
            "code": 400,
            "message": "Bad Request",
            "details": serialized_data.errors
        }}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user=user)
            user_data = LoginSerializer(user).data
            return JsonResponse({
                "status": "success",
                "message": "Login successful",
                "data": {
                    "user": {
                        "email": user_data.get("email"),
                        "first_name": user_data.get("first_name"),
                        "last_name": user_data.get("last_name"),
                        "role": user_data.get("role"),
                        "registration_date": user_data.get("registration_date"),
                        "registration_time": user_data.get("registration_time")
                    },
                    "auth_token": tokens
                }
            }, status=status.HTTP_200_OK)
        return JsonResponse({
            "code": 400,
            "status": "error",
            "message": "Invalid credentials"
        }, status=status.HTTP_400_BAD_REQUEST)


class LogoutUser(GenericAPIView):
    def post(self, request):
        email = request.data.get("email")
        if email is None:
            return JsonResponse(
                {"error": "Please provide email"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = DiveUser.objects.get(email=email)
            user.auth_token.delete()
            return JsonResponse(
                {"status": "success", "message": f"User {user.email} logged out successfully"},
                status=status.HTTP_200_OK,
            )
        except DiveUser.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "User does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
