from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("calculator/", views.calculation, name='calculation'),
    path('delete/<int:pk>/', views.delete_data, name='delete_data'),
]