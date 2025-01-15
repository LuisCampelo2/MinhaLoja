from django.shortcuts import render,redirect,get_object_or_404
from products.models import Produto
from django.contrib.auth.decorators import login_required
from .models import Carrinho,ItemPedido
from django.http import Http404
from users.models import CustomUser
from django.db import IntegrityError

# Create your views here.

def meusPedidos(request):
    return render(request,'orders/pages/meuspedidos.html')

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    
    # Obter ou criar o carrinho do usuário (sem o total como condição)
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)

    # Verificar se o produto já está no carrinho
    item_pedido, created = ItemPedido.objects.get_or_create(
        carrinho=carrinho,
        produto=produto,
        defaults={'quantidade': 1, 'preco': produto.preco}  # Definir quantidade inicial como 1
    )

    # Se o item já existia, apenas aumenta a quantidade
    if not created:
        item_pedido.quantidade += 1
        item_pedido.save()

    # Atualizar o total do carrinho
    total_carrinho = sum(item.total() for item in carrinho.itempedido_set.all())
    carrinho.total = total_carrinho
    carrinho.save()
    
    return redirect('orders:carrinho')

@login_required
def carrinho(request):
    usuario = request.user  # Usuário logado

    # Certifique-se de que o usuário existe
    usuario = get_object_or_404(CustomUser, id=usuario.id)

   
        # Tente obter ou criar um carrinho para o usuário, passando o total inicialmente
    carrinho, created = Carrinho.objects.get_or_create(
    usuario=usuario,
    defaults={"total": 0.00}  # Certifique-se de que o total é inicializado
    )
    
     

    context = {
        'carrinho': carrinho,
    }
    return render(request, 'orders/pages/carrinho.html', context)


def removeritem(request,id):
   try:
        item_pedido = ItemPedido.objects.get(id=id)
   except ItemPedido.DoesNotExist:
        raise Http404("Item não encontrado.")  # Ou você pode redirecionar com uma mensagem de erro

   carrinho = item_pedido.carrinho
   item_pedido.delete()

    # Atualizar o total do carrinho após remoção
   itens_do_carrinho = carrinho.itempedido_set.all()  # Obter todos os itens restantes
   total_carrinho = sum(item.total() for item in itens_do_carrinho)

    # Se o carrinho ficar vazio, o total será 0
   carrinho.total = total_carrinho if itens_do_carrinho else 0.00
   carrinho.save()

   return redirect('orders:carrinho')
