from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = RichTextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True)
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