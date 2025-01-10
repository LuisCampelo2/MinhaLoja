from django.contrib import admin
from .models import Carrinho, ItemPedido
from products.models import Produto

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1  # Quantidade de linhas extras para adicionar um ItemPedido
    fields = ['produto', 'quantidade', 'preco']

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total', 'data_criacao')  # Agora 'data_criacao' é um campo válido
    list_filter = ('usuario',)
    search_fields = ('usuario__username',)
    inlines = [ItemPedidoInline]  # Exibindo os itens do carrinho diretamente no admin

