from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
    TimeField,
)
from authentication.models import DiveUser


class ResponseSerializer(ModelSerializer):
    id = IntegerField(required=False, read_only=True)
    last_name = CharField(required=False, read_only=True)
    first_name = CharField(read_only=True, required=False)
    registration_time = TimeField(required=False, read_only=True)
    role = CharField(required=False, read_only=True)
    email = CharField(required=False, read_only=True)

    class Meta:
        model = DiveUser
        fields = ["id", "first_name", "last_name", "email", "registration_time", "role"]
