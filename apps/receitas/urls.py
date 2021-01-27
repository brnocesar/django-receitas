from django.urls import path
from .src.controller import *

urlpatterns = [
    path('', index, name='receita.index'),
    path('receitas/criar', create, name='receita.create'),
    path('receitas/<int:receita_id>', show, name='receita.show'),
    path('receitas/editar/<int:receita_id>', edit, name='receita.edit'),
    path('receitas/deletar/<int:receita_id>', destroy, name='receita.destroy'),
    # rota para o campo de busca
]