from django.contrib import admin
from .models import Receita

class IndexReceita(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'tempo_preparo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_per_page = 10

admin.site.register(Receita, IndexReceita)
