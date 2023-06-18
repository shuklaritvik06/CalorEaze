from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import CalorieModel


class CalorieAdmin(ModelAdmin):
    readonly_fields = ('date', 'time')
    list_display = ["user_id", "query", "total_calories", "time", "date", "met_expectations", "id"]
    search_fields = ["user_id"]


admin.site.register(CalorieModel, CalorieAdmin)
