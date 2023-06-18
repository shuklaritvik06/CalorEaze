from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import ExpectedCalories


class ExpectedAdmin(ModelAdmin):
    list_display = ["user_id", "expected", "created_at", "updated_at", "id"]
    search_fields = ["user_id"]


admin.site.register(ExpectedCalories, ExpectedAdmin)
