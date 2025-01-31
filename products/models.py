from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = CKEditor5Field("Descrição", config_name="default")
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    CATEGORIAS = [
        ('eletronicos', 'Eletrônicos'),
        ('roupas', 'Roupas'),
        ('livros', 'Livros'),
        ('esportes', 'Esportes'),
        ('outros', 'Outros'),
    ]

    # Campo de categoria com opções
    categoria = models.CharField(
        max_length=50, 
        choices=CATEGORIAS, 
        default='outros'
    )
    def __str__(self):
        return self.nome
    
class ProdutoImagem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return f"Imagem de {self.produto.nome}"