from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import stripe
from orders.models import Carrinho
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
@csrf_exempt  # Para permitir requisições POST via fetch
def create_payment(request):
    if request.method == "POST":
        try:
            import json
            data = json.loads(request.body)

            # Total em centavos
            total = int(float(data.get("total", 0)) * 100)

            # Cria um PaymentIntent no Stripe
            intent = stripe.PaymentIntent.create(
                amount=total,
                currency='brl',
                payment_method_types=['card'],
            )

            return JsonResponse({'client_secret': intent['client_secret']})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método não permitido'}, status=405)


# views.py


def checkout_view(request):
    # Exemplo de valor total
    total = 123.45  # O valor do total pode vir do banco de dados ou ser calculado
    context = {
        'total': total,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'pagamento/pagamento.html', context)
