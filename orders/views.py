from django.shortcuts import render,redirect
from products.models import Produto
from django.contrib.auth.decorators import login_required
from .models import Carrinho,ItemPedido
from django.http import Http404
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
    # Verifica se o carrinho do usuário já existe
    carrinho = Carrinho.objects.filter(usuario=request.user).first()

    # Se não existir, cria um novo carrinho
    if not carrinho:
        carrinho = Carrinho(usuario=request.user)
        carrinho.save()

    # Obtém todos os itens do carrinho
    itens_do_carrinho = carrinho.itempedido_set.all()

    # Calcula o total do carrinho
    total_carrinho = sum(item.total() for item in itens_do_carrinho)

    # Atualiza o total no objeto Carrinho
    carrinho.total = total_carrinho
    carrinho.save()

    # Verifica se o carrinho está vazio
    carrinho_vazio = not itens_do_carrinho.exists()

    return render(request, 'orders/pages/carrinho.html', {
        'carrinho': carrinho,
        'itens_do_carrinho': itens_do_carrinho,
        'carrinho_vazio': carrinho_vazio,
        'total_carrinho': total_carrinho
    })
    
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
