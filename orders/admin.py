from django.contrib import admin
from .models import Carrinho, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1  # Número de linhas adicionais para adicionar novos itens diretamente no admin
    fields = ('produto', 'quantidade', 'preco', 'total')  # Campos que aparecem no inline
    readonly_fields = ('total',)  # Campo que será somente leitura

    def total(self, obj):
        return obj.total()  # Exibe o total diretamente no admin

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'data_criacao', 'calcular_total')  # Colunas na listagem
    list_filter = ('data_criacao',)  # Filtros laterais no admin
    search_fields = ('usuario__username', 'usuario__email')  # Campos para busca
    inlines = [ItemPedidoInline]  # Adiciona o inline dos itens do pedido

    def calcular_total(self, obj):
        return obj.calcular_total()  # Exibe o total calculado do carrinho

    calcular_total.short_description = 'Total do Carrinho'

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'carrinho', 'produto', 'quantidade', 'preco', 'total')  # Colunas na listagem
    list_filter = ('carrinho', 'produto')  # Filtros laterais no admin
    search_fields = ('carrinho__usuario__username', 'produto__nome')  # Campos para busca

    def total(self, obj):
        return obj.total()  # Exibe o total calculado do item

    total.short_description = 'Total do Item'


