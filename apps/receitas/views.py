from django.shortcuts import render

def index(request):
    
    receitas = {
        1: 'Vitamina de Banana',
        2: 'Nhoque de Batatinha',
        3: 'Bolo de Cenoura'
    }
    dados = {'nome_das_receitas': receitas}
    
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
