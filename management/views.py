from rest_framework.generics import GenericAPIView
from drf_yasg.utils import swagger_auto_schema
from authentication.models import DiveUser
from authentication.serializer import RegisterSerializer
from django.http import JsonResponse
from rest_framework import status
from .serializer import ResponseSerializer
from .permissions import ManagementPerms
from rest_framework.permissions import IsAuthenticated


class CreateView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [ManagementPerms]

    @swagger_auto_schema(
        tags=["users"],
        operation_summary="Create a new user",
        operation_description="This endpoint is for user manager to create a user",
    )
    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(
                {
                    "status": "success",
                    "code": 201,
                    "message": "User created successfully",
                    "data": serialized_data.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return JsonResponse(
            {
                "error": {
                    "code": 400,
                    "message": "Bad Request",
                    "details": serialized_data.errors,
                }
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class UpdateView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [ManagementPerms]

    @swagger_auto_schema(
        tags=["users"],
        operation_summary="Update a user",
        operation_description="This endpoint is for user manager to update a user",
    )
    def put(self, request, id):
        try:
            instance = DiveUser.objects.filter(pk=id).first()
        except DiveUser.DoesNotExist:
            return JsonResponse(
                {"status": "error", "code": 404, "message": "Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serialized_data = self.serializer_class(instance, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(
                {
                    "status": "success",
                    "code": 201,
                    "message": "User updated successfully",
                    "data": serialized_data.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return JsonResponse(
            {
                "error": {
                    "code": 400,
                    "message": "Bad Request",
                    "details": serialized_data.errors,
                }
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class FilterView(GenericAPIView):
    serializer_class = ResponseSerializer
    permission_classes = [ManagementPerms]

    @swagger_auto_schema(
        tags=["users"],
        operation_summary="Filter user",
        operation_description="This endpoint is for user manager to filter user",
    )
    def get(self, request, id):
        instance = DiveUser.objects.filter(pk=id).first()
        if instance is not None:
            serialized_data = self.serializer_class(instance)
            return JsonResponse(
                {"status": "success", "data": serialized_data.data},
                status=status.HTTP_200_OK,
            )
        return JsonResponse(
            {"status": "error", "code": 404, "message": "Not Found"},
            status=status.HTTP_404_NOT_FOUND,
        )


class DeleteView(GenericAPIView):
    serializer_class = ResponseSerializer
    permission_classes = [ManagementPerms]

    @swagger_auto_schema(
        tags=["users"],
        operation_summary="Delete user",
        operation_description="This endpoint is for user manager to delete a user",
    )
    def delete(self, request, id):
        instance = DiveUser.objects.filter(pk=id).first()
        if instance is not None:
            if instance.role == "ADMIN":
                return JsonResponse(
                    {"error": "You can not delete admin user"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            temp = instance
            data = self.serializer_class(temp)
            instance.delete()
            return JsonResponse(
                {"status": "success", "data": data.data},
                status=status.HTTP_204_NO_CONTENT,
            )
        return JsonResponse(
            {"status": "error", "code": 404, "message": "Not Found"},
            status=status.HTTP_404_NOT_FOUND,
        )
