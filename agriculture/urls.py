# myapp/urls.py or smart_agriculture/urls.py (depending on where you're configuring admin)

from django.urls import path, include
from django.contrib import admin  # <-- This import is required for admin.site.urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # This will work after the import
    path('display/', views.display_data, name='dashboard'),
    path('api/analyze/', views.process_and_analyze, name='process_and_analyze'),
    path('sensors/', include('sensors.urls')),
    path('plant-health/', views.plant_health_view, name='plant_health'),
    path('process-analyze/', views.process_and_analyze, name='process_analyze'),
    path('', include('agriculture.urls')),  # Include URLs from agriculture app
    path('', views.display_data, name='dashboard'),
    path('send/', views.send_to_arduino, name='send_to_arduino'), 

    
]
