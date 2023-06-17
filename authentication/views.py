from rest_framework.generics import GenericAPIView
from .serializer import RegisterSerializer, LoginSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate
from .token import create_jwt_pair_for_user
from rest_framework import status
from pytz import timezone
from datetime import datetime


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []

    def get(self, request):
        return JsonResponse({
            "status": "success",
            "code": 200,
            "message": "Please use POST method to register a user",
        })

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

    def get(self, request):
        return JsonResponse({
            "status": "success",
            "code": 200,
            "message": "Please use POST method to login a user",
        })

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user=user)
            return JsonResponse({
                "status": "success",
                "message": "Login successful",
                "data": {
                    "user": LoginSerializer(user).data,
                    "auth_token": tokens
                }
            }, status=status.HTTP_200_OK)
        return JsonResponse({
            "code": 400,
            "status": "error",
            "message": "Invalid credentials"
        }, status=status.HTTP_400_BAD_REQUEST)
