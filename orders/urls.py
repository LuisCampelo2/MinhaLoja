from django.contrib import admin
from django.urls import path
from . import views

app_name='orders'

urlpatterns = [
    path('meuspedidos/',views.meusPedidos,name="meuspedidos"),
    path('carrinho/',views.carrinho,name="carrinho"),
    path('adicionar_ao_carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('removeritem/<int:id>/',views.removeritem,name='removeritem'),
]