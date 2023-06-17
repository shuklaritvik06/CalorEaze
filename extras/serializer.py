from rest_framework.serializers import ModelSerializer
from .models import ExpectedCalories
from rest_framework.serializers import DateTimeField


class ExpectedSerializer(ModelSerializer):
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)

    class Meta:
        model = ExpectedCalories
        fields = ["user_id", "expected", "created_at", "updated_at"]
