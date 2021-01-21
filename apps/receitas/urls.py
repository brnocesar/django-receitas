from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receitas/<int:receita_id>', views.receita, name='receita'),
    path('receitas/criar', views.create, name='receita.create'),
]