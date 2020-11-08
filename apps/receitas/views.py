from django.shortcuts import render, get_object_or_404
from .models import Receita

def index(request):
    
    receitas = Receita.objects.filter(publicada=True).order_by('-data_criacao')
    
    return render(request, 'index.html', {'receitas': receitas})

def receita(request, receita_id):
    return render(request, 'receita.html', {'receita': get_object_or_404(Receita, pk=receita_id)})
