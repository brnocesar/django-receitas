from django.db import models
from datetime import datetime
from apps.pessoas.models import Pessoa

class Receita(models.Model):
    pessoa        = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=False, default='')
    nome          = models.CharField(max_length=200)
    ingredientes  = models.TextField()
    modo_preparo  = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento    = models.CharField(max_length=100)
    categoria     = models.CharField(max_length=100)
    data_criacao  = models.DateTimeField(default=datetime.now, blank=True)
    publicada     = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
