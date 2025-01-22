from django.urls import path
from .views import *

app_name='pagamento'

urlpatterns = [
    path('',criar_pagamento, name='processar-pagamento'),
]
