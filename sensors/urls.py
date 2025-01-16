from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Root path to dashboard view

]
