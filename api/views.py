from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render


def home_view(request):
    return render(request, "index.html", {"status": "UP"})


@swagger_auto_schema(
    methods=["get"],
    tags=["status"],
    operation_summary="Get API status",
    operation_description="This endpoint is for getting current status of a API",
)
@api_view(["GET"])
def status_view(request):
    return JsonResponse(
        {
            "status": "success",
            "code": 200,
            "message": "Calorie API is running smoothly",
            "data": {"version": "1.0.0", "timestamp": timezone.now()},
        }
    )
