from django.urls import path
from .src.controller import *

urlpatterns = [
    path('login', login, name='usuarios.login'),
    path('logout', logout, name='usuarios.logout'),
    path('cadastro', create, name='cadastro'),
    path('receitas', dashboard, name='usuarios.dashboard'),
]