from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .models import ExpectedCalories
from .serializer import ExpectedSerializer
from django.http import JsonResponse
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from django.utils import timezone
from .permissions import AnonymousUser


class CheckUserMixin:
    permission_classes = [AnonymousUser]

    def checkId(self, request, id):
        return False if request.user.id == id else True


class CreateView(GenericAPIView):
    serializer_class = ExpectedSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["expected"],
        operation_summary="Create a expected calories setting",
        operation_description="This endpoint is for creating a setting of expected calories value",
    )
    def post(self, request):
        serialized_data = self.serializer_class(
            data=request.data, context={"request": request}
        )
        instance = ExpectedCalories.objects.filter(user_id=request.user.id).first()
        if instance is not None:
            return JsonResponse({"message": "Entry already exists for this user id"})
        if serialized_data.is_valid():
            serialized_data.save()
            data = serialized_data.data
            return JsonResponse(
                {
                    "status": "success",
                    "code": 200,
                    "data": {
                        "user_id": data.get("user_id").id,
                        "expected": data.get("expected"),
                        "created_at": data.get("created_at"),
                        "updated_at": data.get("updated_at"),
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        return JsonResponse(
            {"status": "error", "code": 400, "errors": serialized_data.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class FilterView(CheckUserMixin, APIView):
    @swagger_auto_schema(
        tags=["expected"],
        operation_summary="Filter the expected calorie setting using user id",
        operation_description="Filter user expected calories",
    )
    def get(self, request, id):
        if self.checkId(request, id):
            return JsonResponse(
                {"error": "You can only access your data"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        instance = ExpectedCalories.objects.filter(user_id=id).first()
        if instance is not None:
            return JsonResponse(
                {
                    "status": "success",
                    "code": 200,
                    "data": {
                        "user_id": instance.user_id.id,
                        "expected": instance.expected,
                    },
                },
                status=status.HTTP_200_OK,
            )
        return JsonResponse(
            {"status": "error", "code": 404, "errors": "Not Found"},
            status=status.HTTP_404_NOT_FOUND,
        )


class UpdateView(CheckUserMixin, GenericAPIView):
    serializer_class = ExpectedSerializer

    @swagger_auto_schema(
        tags=["expected"],
        operation_summary="Update a expected calories setting",
        operation_description="This endpoint is for updating a setting of expected calories value",
    )
    def put(self, request, id):
        if self.checkId(request, id):
            return JsonResponse(
                {"error": "You can only access your data"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = ExpectedCalories.objects.filter(user_id=id).first()
        if data is not None:
            data.expected = request.data.get("expected")
            data.updated_at = timezone.now()
            data.save()
            return JsonResponse(
                {"status": "success", "code": 200, "message": "Updated Successfully!"},
                status=status.HTTP_200_OK,
            )
        return JsonResponse(
            {"status": "error", "code": 400, "errors": "Something went wrong!"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class DeleteView(CheckUserMixin, APIView):
    @swagger_auto_schema(
        tags=["expected"],
        operation_summary="Delete the expected calorie setting using user id",
        operation_description="Delete user expected calories",
    )
    def delete(self, request, id):
        if self.checkId(request, id):
            return JsonResponse(
                {"error": "You can only access your data"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        instance = ExpectedCalories.objects.filter(user_id=id).first()
        if instance is not None:
            temp = instance
            instance.delete()
            return JsonResponse(
                {
                    "status": "success",
                    "code": 200,
                    "data": {"user_id": temp.user_id.id, "expected": temp.expected},
                },
                status=status.HTTP_200_OK,
            )
        return JsonResponse(
            {"status": "error", "code": 404, "errors": "Not Found"},
            status=status.HTTP_404_NOT_FOUND,
        )
