# smart_agriculture/urls.py

from django.contrib import admin
from django.urls import path, include
from agriculture import views  # Import your views from the agriculture app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.display_data, name='dashboard'),  # Root URL mapped to display_data
    path('api/analyze/', views.process_and_analyze, name='process_and_analyze'),  # Your API endpoint
    path('sensors/', include('sensors.urls')),  # Ensure this line is included
]
