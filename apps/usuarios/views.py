from django.shortcuts import render

def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def dashboard(request):
    pass
