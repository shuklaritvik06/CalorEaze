from django.urls import path
from .views import CreateView, FilterView, UpdateView, DeleteView

urlpatterns = [
    path("expected/<int:id>/", FilterView.as_view()),
    path("expected/create/", CreateView.as_view()),
    path("expected/update/<int:id>/", UpdateView.as_view()),
    path("expected/delete/<int:id>/", DeleteView.as_view()),
]
