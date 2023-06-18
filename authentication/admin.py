from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import DiveUser


class DiveUserAdmin(ModelAdmin):
    readonly_fields = ('registration_date', 'registration_time')
    search_fields = ["role", "email"]
    list_display = ["username", "email", "registration_date", "registration_time", "role"]


admin.site.register(DiveUser, DiveUserAdmin)
