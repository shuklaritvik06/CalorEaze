from rest_framework.serializers import ModelSerializer, CharField, TimeField, DateField
from .models import DiveUser
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class RegisterSerializer(ModelSerializer):
    email = CharField(max_length=100)
    username = CharField(max_length=45)
    password = CharField(min_length=8, write_only=True)
    registration_time = TimeField()

    class Meta:
        model = DiveUser
        fields = ["username", "email", "password", "registration_date",
                  "registration_time", "first_name", "last_name", "role"]

    def validate(self, attrs):
        email_exists = DiveUser.objects.filter(email=attrs["email"])
        if email_exists:
            raise ValidationError("Email is already registered")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class LoginSerializer(ModelSerializer):
    email = CharField(max_length=100)

    class Meta:
        model = DiveUser
        fields = ["email", "role", "first_name", "last_name"]

    def validate(self, attrs):
        email_exists = DiveUser.objects.filter(email=attrs["email"])
        if email_exists is None:
            raise ValidationError("Email does not exist")
        return super().validate(attrs)

