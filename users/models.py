from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name='CPF',
        help_text='Insira o CPF com 11 dígitos numéricos',
    )
    telefone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone',
        help_text='Insira o telefone no formato (XX) XXXXX-XXXX',
    )
    data_nascimento = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Nascimento',
    )
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Prefiro não informar'),
    ]
    genero = models.CharField(
        max_length=1,
        choices=GENERO_CHOICES,
        default='N',  # Define "Prefiro não informar" como padrão
        verbose_name='Gênero',
)

    def __str__(self):
        return self.username  # ou outro campo como o 'first_name'

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
