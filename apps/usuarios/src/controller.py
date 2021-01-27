from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from apps.receitas.models import Receita
from .validacoes import *

def create(request):
    if request.method == 'POST':
        nome                  = request.POST['nome']
        email                 = request.POST['email']
        password              = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        erros = 0
        if campo_vazio(nome):
            messages.error(request, 'Campo nome é obrigratório!')
            erros += 1
        if campo_vazio(email):
            messages.error(request, 'Campo email é obrigratório!')
            erros += 1
        if usuario_cadastrado(nome, email):
            messages.error(request, 'Usuário já é cadastrado!')
            erros += 1
        if campo_vazio(password):
            messages.error(request, 'Campo senha é obrigratório!')
            erros += 1
        if senhas_diferentes(password, password_confirmation):
            messages.error(request, 'As senhas devem ser iguais!')
            erros += 1
        if erros > 0:
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        messages.success(request, f"Usuário {user.username} cadastrado com sucesso!")

        return redirect('usuarios.login')
    
    return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email    = request.POST['email']
        password = request.POST['password']
        
        if campo_vazio(email) or campo_vazio(password):
            messages.error(request, 'Todos os campos são obrigratórios!')
            return redirect('usuarios.login')
    
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request=request, username=nome, password=password)
            
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                
                return redirect('usuarios.dashboard')
        
    return render(request, 'usuarios/login.html')

def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Realize login para acessar a dashboard!')
        return redirect('login')
    
    receitas = Receita.objects.filter(pessoa=request.user.id).order_by('data_criacao')
    
    return render(request, 'usuarios/dashboard.html', {'receitas': receitas})

def logout(request):
    auth.logout(request)
    return redirect('receita.index')
