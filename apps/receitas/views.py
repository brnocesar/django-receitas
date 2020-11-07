from django.shortcuts import render, get_object_or_404
from .models import Receita

def index(request):
    return render(request, 'index.html', {'receitas': Receita.objects.all()})

def receita(request, receita_id):
    return render(request, 'receita.html', {'receita': get_object_or_404(Receita, pk=receita_id)})
