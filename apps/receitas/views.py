from django.shortcuts import render
from .models import Receita

def index(request):
    return render(request, 'index.html', {'receitas': Receita.objects.all()})

def receita(request):
    return render(request, 'receita.html')
