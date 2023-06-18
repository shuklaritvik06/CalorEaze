from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .permissions import CorePerms
from .serializer import CalorieSerializer, CoreResponseSerializer
from django.http import JsonResponse
from rest_framework import status
from .models import CalorieModel
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView


class CreateView(GenericAPIView):
    serializer_class = CalorieSerializer
    permission_classes = [CorePerms]

    @swagger_auto_schema(
        tags=['calories'],
        operation_summary='Add daily calories',
    )
    def post(self, request):
        serialized_data = self.serializer_class(data=request.data, context={'request': request})
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({
                "status": "success",
                "code": 200,
                "message": "Calories Data Saved Successfully!"
            }, status=status.HTTP_201_CREATED)
        return JsonResponse({
            "status": "error",
            "code": 400,
            "message": serialized_data.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateView(GenericAPIView):
    serializer_class = CalorieSerializer
    permission_classes = [CorePerms]

    @swagger_auto_schema(
        tags=['calories'],
        operation_summary='Update daily calories',
    )
    def put(self, request, id):
        instance = CalorieModel.objects.filter(pk=id).first()
        if instance is not None and instance.user_id.id != request.user.id:
            return JsonResponse({
                "error": "You can only access your data"
            }, status=status.HTTP_400_BAD_REQUEST)
        if instance is None:
            return JsonResponse({
                "status": "error",
                "code": 404,
                "message": "Not Found!"
            }, status=status.HTTP_404_NOT_FOUND)

        serialized_data = self.serializer_class(instance, data=request.data, context={'request': request})
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({
                "status": "success",
                "code": 200,
                "message": "Calories Data Updated Successfully!"
            }, status=status.HTTP_200_OK)
        return JsonResponse({
            "status": "error",
            "code": 400,
            "message": serialized_data.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class DeleteView(APIView):
    permission_classes = [CorePerms]

    @swagger_auto_schema(
        tags=['calories'],
        operation_summary='Delete daily calories',
    )
    def delete(self, request, id):
        instance = CalorieModel.objects.filter(pk=id).first()
        if instance is not None and instance.user_id.id != request.user.id:
            return JsonResponse({
                "error": "You can only access your data"
            }, status=status.HTTP_400_BAD_REQUEST)
        if instance is None:
            return JsonResponse({
                "status": "error",
                "code": 404,
                "message": "Not Found!"
            }, status=status.HTTP_404_NOT_FOUND)
        temp = instance
        instance.delete()
        return JsonResponse({
            "status": "success",
            "code": 204,
            "message": "Calories Data Deleted Successfully!"
        }, status=status.HTTP_204_NO_CONTENT)


class FilterView(GenericAPIView):
    serializer_class = CoreResponseSerializer
    permission_classes = [CorePerms]

    @swagger_auto_schema(
        tags=['calories'],
        operation_summary='Filter daily calories',
    )
    def get(self, request, id):
        instance = CalorieModel.objects.filter(pk=id).first()
        if instance is not None and instance.user_id.id != request.user.id:
            return JsonResponse({
                "error": "You can only access your data"
            }, status=status.HTTP_400_BAD_REQUEST)
        if instance is None:
            return JsonResponse({
                "status": "error",
                "code": 404,
                "message": "Not Found!"
            }, status=status.HTTP_404_NOT_FOUND)
        data = self.serializer_class(instance).data
        return JsonResponse({
            "status": "success",
            "code": 200,
            "message": {
                "user_id": data.get("user_id").id,
                "query": data.get("query"),
                "time": data.get("time"),
                "date": data.get("date"),
                "total_calories": data.get("total_calories"),
                "met_expectations": data.get("met_expectations")
            }
        }, status=status.HTTP_200_OK)


class FilterByUserId(ListAPIView):
    serializer_class = CalorieSerializer
    queryset = CalorieModel.objects.all()

    @swagger_auto_schema(
        tags=['calories'],
        operation_summary='Filter user calories',
    )
    def get(self, request):
        entries = CalorieModel.objects.filter(user_id=request.user.id)
        data = []
        for i in entries:
            data.append({
                "query": i.query,
                "total_calories": i.total_calories,
                "date": i.date,
                "time": i.time,
                "id": i.id
            })
        return JsonResponse({"data": data, "met_expectations": entries[0].met_expectations or False},
                            status=status.HTTP_200_OK)

