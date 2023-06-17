from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.utils import timezone


@api_view(["GET"])
def status_view(request):
    return JsonResponse({
        "status": "success",
        "code": 200,
        "message": "Calorie API is running smoothly",
        "data": {
            "version": "1.0.0",
            "timestamp": timezone.now()
        }
    })
