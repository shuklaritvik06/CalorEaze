from django.urls import path
from .views import CreateView, UpdateView, DeleteView, FilterView, FilterByUserId

urlpatterns = [
    path('filter/<int:id>/', FilterView.as_view()),
    path('create/', CreateView.as_view()),
    path('delete/<int:id>/', DeleteView.as_view()),
    path('update/<int:id>/', UpdateView.as_view()),
    path('own/', FilterByUserId.as_view())
]