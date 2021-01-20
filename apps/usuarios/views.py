from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        email    = request.POST['email']
        password = request.POST['password']
        
        if not email.strip() or not password.strip():
            print('=> Todos os campos são obrigratórios!')
            return redirect('login')
    
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request=request, username=nome, password=password)
            
            if user is not None:
                auth.login(request, user)
                print('=> Login realizado com sucesso!')
                
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
            print('=> Campo nome é obrigratório!')
            erros += 1
        if not email.strip():
            print('=> Campo email é obrigratório!')
            erros += 1
        if not password.strip():
            print('=> Campo senha é obrigratório!')
            erros += 1
        if password != password_confirmation:
            print('=> As senhas devem ser iguais!')
            erros += 1
        if User.objects.filter(email=email).exists():
            print('=> Usuário já é cadastrado!')
            erros += 1
        if erros > 0:
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        print('=> Usuário cadastrado com sucesso!')

        return redirect('login')
    
    return render(request, 'usuarios/cadastro.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    
    return redirect('index')
