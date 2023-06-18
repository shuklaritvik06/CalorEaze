from django.db import models
from authentication.models import DiveUser


class CalorieModel(models.Model):
    user_id = models.ForeignKey(DiveUser, on_delete=models.CASCADE, null=True)
    query = models.TextField(blank=True)
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    total_calories = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    met_expectations = models.BooleanField(default=False)

