from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class DiveUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email is Required')
        if not password:
            raise ValueError('Password is Required')
        email = self.normalize_email(email=email)
        user = self.model(
            email=email,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("role", "ADMIN")
        return self.create_user(email=email, password=password, **kwargs)


class DiveUser(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45, unique=True)
    role = models.CharField(max_length=100, choices=(('REGULAR', 'REGULAR'),
                                                     ('MANAGER', 'MANAGER'), ('ADMIN', 'ADMIN')), default="REGULAR")
    registration_date = models.DateField(auto_now=True)
    registration_time = models.TimeField(null=True)

    objects = DiveUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return super().username
