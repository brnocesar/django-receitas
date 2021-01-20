from django.shortcuts import render, redirect

def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        print(nome, email, password, password_confirmation)
        print(request.POST)
        return redirect('login')
    
    return render(request, 'usuarios/cadastro.html')

def dashboard(request):
    pass
