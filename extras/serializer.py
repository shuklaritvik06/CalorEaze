from rest_framework.serializers import ModelSerializer
from .models import ExpectedCalories
from rest_framework.serializers import DateTimeField
from django.utils import timezone


class ExpectedSerializer(ModelSerializer):
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)

    class Meta:
        model = ExpectedCalories
        fields = ["user_id", "expected", "created_at", "updated_at"]

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now()
