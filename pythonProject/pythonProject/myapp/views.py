from django.shortcuts import render
from .models import LicencaAmbiental

def dashboard(request):
    # Recupere todas as licenças ambientais do banco de dados
    licencas = LicencaAmbiental.objects.all()

    # Passe os dados para o template
    context = {'licencas': licencas}
    return render(request, 'dash_apps/dashboard.html', context)
