from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import CalorieModel


class CalorieAdmin(ModelAdmin):
    readonly_fields = ('date', 'time')
    list_display = ["user_id", "text", "total_calories", "time", "date", "met_expectations"]
    search_fields = ["user_id"]


admin.site.register(CalorieModel, CalorieAdmin)
