from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import stripe
from orders.models import Carrinho
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import mercadopago
from project import settings



stripe.api_key = settings.STRIPE_SECRET_KEY
ACCESS_TOKEN = settings.MERCADO_PAGO_TOKEN

sdk = mercadopago.SDK(ACCESS_TOKEN)

@login_required
@csrf_exempt
def create_pix_payment(request):
    if request.method == "POST":
        try:
            carrinho = Carrinho.objects.get(usuario=request.user)
            total = carrinho.calcular_total()

            # Dados para a criação do pagamento
            payment_data = {
                "transaction_amount": float(total),  # Total do carrinho
                "description": "Compra na Minha Loja",
                "payment_method_id": "pix",
                "payer": {
                    "email": request.user.email,  # Email do usuário autenticado
                    "first_name": request.user.first_name,
                    "last_name": request.user.last_name,
                }
            }

            # Cria o pagamento
            payment_response = sdk.payment().create(payment_data)
            payment = payment_response["response"]

            # Retorna os dados do PIX, incluindo o QR Code
            return JsonResponse({
                "id": payment["id"],
                "status": payment["status"],
                "qr_code_base64": payment["point_of_interaction"]["transaction_data"]["qr_code_base64"],
                "qr_code": payment["point_of_interaction"]["transaction_data"]["qr_code"],
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método não permitido"}, status=405)

@login_required
@csrf_exempt  # Para permitir requisições POST via fetch
def create_payment_card(request):
    if request.method == "POST":
        try:
            carrinho=Carrinho.objects.get(usuario=request.user)
            total = carrinho.calcular_total()  
            # Cria um PaymentIntent no Stripe
            intent = stripe.PaymentIntent.create(
                amount=int(total*100),
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
    carrinho=Carrinho.objects.get(usuario=request.user)
    total = carrinho.calcular_total()  # O valor do total pode vir do banco de dados ou ser calculado
    context = {
        'total': total,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'pagamento/pagamento.html', context)
