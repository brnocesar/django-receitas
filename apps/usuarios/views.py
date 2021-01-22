from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from apps.receitas.models import Receita

def login(request):
    if request.method == 'POST':
        email    = request.POST['email']
        password = request.POST['password']
        
        if not email.strip() or not password.strip():
            messages.error(request, 'Todos os campos são obrigratórios!')
            return redirect('login')
    
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request=request, username=nome, password=password)
            
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                
                return redirect('dashboard')
        
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def cadastro(request):
    if request.method == 'POST':
        nome                  = request.POST['nome']
        email                 = request.POST['email']
        password              = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        erros = 0
        if not nome.strip():
            messages.error(request, 'Campo nome é obrigratório!')
            erros += 1
        if not email.strip():
            messages.error(request, 'Campo email é obrigratório!')
            erros += 1
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já é cadastrado!')
            erros += 1
        if not password.strip():
            messages.error(request, 'Campo senha é obrigratório!')
            erros += 1
        if password != password_confirmation:
            messages.error(request, 'As senhas devem ser iguais!')
            erros += 1
        if erros > 0:
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        messages.success(request, f"Usuário {user.username} cadastrado com sucesso!")

        return redirect('login')
    
    return render(request, 'usuarios/cadastro.html')

def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Realize login para acessar a dashboard!')
        return redirect('login')
    
    receitas = Receita.objects.filter(pessoa=request.user.id).order_by('data_criacao')
    
    return render(request, 'usuarios/dashboard.html', {'receitas': receitas})
