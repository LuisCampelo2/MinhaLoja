from django.shortcuts import render
from products.models import Produto,ProdutoImagem


# Create your views here.
def index(request):
    produtos = Produto.objects.all()

    # Passar os produtos para o template
    return render(request, 'home/pages/index.html', {'produtos': produtos})

def search_view(request):
    produto=Produto.objects.all()
    
    query = request.GET.get('q')  # Obtém o termo de busca do parâmetro 'q'
    resultados = []

    if query:
        resultados = Produto.objects.filter(nome__icontains=query)  # Busca produtos com nomes semelhantes ao termo

    return render(request, 'home/pages/search.html', {'resultados': resultados, 'query': query ,'produto':produto})