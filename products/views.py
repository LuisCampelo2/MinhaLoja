from django.shortcuts import render
from .models import Produto,ProdutoImagem

# Create your views here.
def produto_view(request,id):
    produto=Produto.objects.get(id=id)
    imagem=ProdutoImagem.objects.get(id=id)
    context={
        'produto':produto,
        'imagem':imagem,
    }
    return render(request,'products/products.html',context)