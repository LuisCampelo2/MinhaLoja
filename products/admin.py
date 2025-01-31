from django.contrib import admin
from .models import Produto, ProdutoImagem

class ProdutoImagemInline(admin.TabularInline):  # Ou StackedInline para outra visualização
    model = ProdutoImagem
    extra = 1  # Quantidade de campos extras para adicionar novas imagens

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'estoque')
    inlines = [ProdutoImagemInline]  # Adiciona as imagens dentro do Produto no admin

@admin.register(ProdutoImagem)
class ProdutoImagemAdmin(admin.ModelAdmin):
    list_display = ('produto', 'imagem')

  