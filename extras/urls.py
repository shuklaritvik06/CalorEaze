from django.urls import path
from .views import CaloriesView, FilterView

urlpatterns = [
    path("expected/<int:id>", FilterView.as_view(), name="filter"),
    path("expected/", CaloriesView.as_view(), name="expected")
]
