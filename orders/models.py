from django.db import models
from django.contrib.auth.models import User
from products.models import Produto  # Adicione a importação do modelo Produto, se necessário
from django.utils import timezone
from users.models import CustomUser

class ItemPedido(models.Model):
    carrinho = models.ForeignKey('Carrinho', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def total(self):
        return self.quantidade * self.preco

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome}'

class Carrinho(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_criacao = models.DateTimeField(default=timezone.now)  # Adicionando data de criação

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'
    

