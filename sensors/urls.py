from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Root path to dashboard view
    path('plant-health/', views.plant_health, name='plant_health'),
]
