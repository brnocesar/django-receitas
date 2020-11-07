from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome          = models.CharField(max_length=200)
    ingredientes  = models.TextField()
    modo_preparo  = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento    = models.CharField(max_length=100)
    categoria     = models.CharField(max_length=100)
    data_criacao  = models.DateTimeField(default=datetime.now, blank=True)
