from django.db import models
from authentication.models import DiveUser


class ExpectedCalories(models.Model):
    user_id = models.OneToOneField(DiveUser, on_delete=models.CASCADE)
    expected = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True)
