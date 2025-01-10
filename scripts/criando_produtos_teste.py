import sys
import os

# Definir o diretório do projeto como parte do caminho de busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Definir o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  # Ajuste se o nome do seu projeto for diferente

import django
django.setup()

from products.models import Produto
from random import choice, randint
from faker import Faker

fake = Faker()

# Gerar 10 produtos aleatórios
for _ in range(10):
    produto = Produto.objects.create(
        nome=fake.word(),
        descricao=fake.text(),
        preco=round(randint(10, 500) + randint(0, 99) / 100, 2),
        estoque=randint(1, 100),
    )
    print(f'Produto criado: {produto.nome}')

