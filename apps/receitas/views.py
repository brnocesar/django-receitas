from django.shortcuts import render, get_object_or_404
from .models import Receita

def index(request):
    
    receitas = Receita.objects.filter(publicada=True)
    
    if 'procurar_receita' in request.GET and request.GET['procurar_receita']:
        receitas = receitas.filter(nome__icontains=request.GET['procurar_receita'])
    
    receitas = receitas.order_by('-data_criacao')
    
    return render(request, 'receitas/index.html', {'receitas': receitas})

def receita(request, receita_id):
    return render(request, 'receitas/receita.html', {'receita': get_object_or_404(Receita, pk=receita_id)})

def create(request):
    return render(request, 'receitas/create.html')