from django.conf import settings
from django.db import models

class Pagamento(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=20, choices=[('cartao', 'Cartão'), ('pix', 'Pix')])
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('sucesso', 'Sucesso'), ('falha', 'Falha')], default='pendente')
    stripe_payment_intent = models.CharField(max_length=100, blank=True, null=True)  # ID do PaymentIntent no Stripe
    data_pagamento = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return f"Pagamento de {self.usuario} - {self.valor}"
