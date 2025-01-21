from django.urls import path
from .views import ProcessarPagamento

app_name='pagamento'

urlpatterns = [
    path('', ProcessarPagamento.as_view(), name='processar-pagamento'),
]
