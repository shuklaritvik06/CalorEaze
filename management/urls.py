from django.urls import path
from .views import CreateView, DeleteView, UpdateView, FilterView

urlpatterns = [
    path('create/', CreateView.as_view(), name="create"),
    path('delete/<int:id>/', DeleteView.as_view(), name="delete"),
    path('update/<int:id>/', UpdateView.as_view(), name="update"),
    path('filter/<int:id>/', FilterView.as_view(), name="filter")
]
