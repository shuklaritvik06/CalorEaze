from django.contrib import admin
from django.urls import path, include
from .views import status_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', status_view),
    path('api/v1/auth/', include("authentication.urls"))
]
