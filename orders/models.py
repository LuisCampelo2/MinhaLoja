from django.db import models
from django.contrib.auth.models import User
from products.models import Produto  # Adicione a importação do modelo Produto, se necessário
from django.utils import timezone
from users.models import CustomUser
from project import settings



class Carrinho(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    data_criacao = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f'Carrinho de {self.usuario.username}'

    def calcular_total(self):
        return sum(item.total() for item in self.itempedido_set.all())
    
class ItemPedido(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def total(self):
        return self.quantidade * self.preco

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome}'
