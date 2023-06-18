from django.db import models
from authentication.models import DiveUser


class ExpectedCalories(models.Model):
    user_id = models.OneToOneField(DiveUser, on_delete=models.CASCADE)
    expected = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
