from django.shortcuts import render, get_object_or_404, redirect
from .models import Receita
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    receitas = Receita.objects.filter(publicada=True)
    
    if 'procurar_receita' in request.GET and request.GET['procurar_receita']:
        receitas = receitas.filter(nome__icontains=request.GET['procurar_receita'])
    
    receitas = receitas.order_by('-data_criacao')
    
    return render(request, 'receitas/index.html', {'receitas': receitas})

def receita(request, receita_id):
    return render(request, 'receitas/receita.html', {'receita': get_object_or_404(Receita, pk=receita_id)})

def create(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Realize login para cadastrar uma receita!')
        return redirect('index')
    
    if request.method == 'POST':
        nome          = request.POST['nome']
        ingredientes  = request.POST['ingredientes']
        modo_preparo  = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento    = request.POST['rendimento']
        categoria     = request.POST['categoria']
        foto          = request.FILES['foto']
        # user          = request.user # porque nao assim?
        user          = get_object_or_404(User, pk=request.user.id)
        
        receita = Receita.objects.create(
            pessoa=user,
            nome=nome,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            rendimento=rendimento,
            categoria=categoria,
            foto=foto
        )
        receita.save()
        messages.success(request, 'Receita cadastrada com sucesso!')
        
        return redirect('dashboard')
    
    return render(request, 'receitas/create.html')

def destroy(request, receita_id):
    # abstrair isso para um metodo que da um retorno mais adequado no caso de nao existir
    # ou usar algo que de pra verificar se nao existe
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    
    return redirect('dashboard')