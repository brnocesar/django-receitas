from django.urls import path
from .src.controller import *
# from .src.controllers.ReceitaController import *

urlpatterns = [
    path('', index, name='receitas.index'),
    path('criar', create, name='receitas.create'),
    path('<int:receita_id>', show, name='receitas.show'),
    path('editar/<int:receita_id>', edit, name='receitas.edit'),
    path('deletar/<int:receita_id>', destroy, name='receitas.destroy'),
    # rota para o campo de busca
]