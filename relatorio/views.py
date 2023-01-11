from django.shortcuts import render
from .models import Sobreviventes, Inventario

def relatorio_geral(request):
    return render(request, 'relatorio_geral.html')


# def relatorio_geral(request):
#     pass