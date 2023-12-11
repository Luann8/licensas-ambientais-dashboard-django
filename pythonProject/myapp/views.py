# myapp/views.py

from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'dash_apps/dashboard.html')
