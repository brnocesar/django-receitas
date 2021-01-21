from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Receita(models.Model):
    pessoa        = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default='')
    nome          = models.CharField(max_length=200)
    ingredientes  = models.TextField()
    modo_preparo  = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento    = models.CharField(max_length=100)
    categoria     = models.CharField(max_length=100)
    data_criacao  = models.DateTimeField(default=datetime.now, blank=True)
    foto          = models.ImageField(upload_to='receitas/fotos/', blank=True)
    publicada     = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
