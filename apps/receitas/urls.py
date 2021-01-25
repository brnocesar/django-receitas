from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receitas/<int:receita_id>', views.receita, name='receita'), # mudar o nome dessa rota para receita.show
    path('receitas/criar', views.create, name='receita.create'),
    path('receitas/deletar/<int:receita_id>', views.destroy, name='receita.destroy'),
]