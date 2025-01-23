from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_payment(request):
    try:
        # Cria um PaymentIntent no Stripe
        intent = stripe.PaymentIntent.create(
            amount=5000,  # Valor em centavos (R$50,00)
            currency='brl',  # Moeda
            payment_method_types=['card'],  # Métodos de pagamento
        )
        return JsonResponse({'client_secret': intent['client_secret']})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=403)

# views.py


def checkout(request):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Retorna um JSON para requisições AJAX
        return JsonResponse({
            'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
        })
    
    # Renderiza o template para requisições normais (não AJAX)
    return render(request, 'pagamento/pagamento.html', {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })
