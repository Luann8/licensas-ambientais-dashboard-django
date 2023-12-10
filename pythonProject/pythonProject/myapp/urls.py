from django.urls import path
from .dash_apps import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]
