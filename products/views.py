from django.shortcuts import render
from .models import Produto

# Create your views here.
def produto_view(request,id):
    produto=Produto.objects.get(id=id)
    context={
        'produto':produto,
    }
    return render(request,'products/products.html',context)