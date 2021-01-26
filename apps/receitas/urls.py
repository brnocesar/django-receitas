from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='receita.index'),
    path('receitas/criar', views.create, name='receita.create'),
    path('receitas/<int:receita_id>', views.show, name='receita.show'),
    path('receitas/editar/<int:receita_id>', views.edit, name='receita.edit'),
    path('receitas/deletar/<int:receita_id>', views.destroy, name='receita.destroy'),
]