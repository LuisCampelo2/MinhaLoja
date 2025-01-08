from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/pages/index.html')

def search_view(request):
    query = request.GET.get('query', '')
    # Lógica de busca aqui (ex: buscar produtos ou itens no banco de dados)
    context = {
        'query': query,
        'results': [],  # Substitua com os resultados da busca
    }
    return render(request, 'home/pages/search_results.html', context)