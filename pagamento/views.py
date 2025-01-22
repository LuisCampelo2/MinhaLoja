import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mercadopago import SDK
from orders.models import Carrinho
from django.conf import settings

# Inicialize o SDK do Mercado Pago
sdk = SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)

@csrf_exempt
def criar_pagamento(request):
    # Recupera o carrinho do usuário
    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
    except Carrinho.DoesNotExist:
        return JsonResponse({"status": "failure", "message": "Carrinho vazio ou não encontrado."}, status=400)

    if request.method == "POST":
        try:
            # Parse do JSON recebido
            data = json.loads(request.body)

            # Validação dos campos obrigatórios
            token = data.get("token")
            payment_method_id = data.get("payment_method_id")
            email = data.get("email")

            if not all([token, payment_method_id, email]):
                return JsonResponse({"status": "failure", "message": "Dados insuficientes para processar o pagamento."}, status=400)

            # Dados do pagamento
            pagamento_data = {
                "transaction_amount": carrinho.total,  # valor do pagamento
                "token": token,
                "description": "Compra no e-commerce",
                "installments": 1,
                "payment_method_id": payment_method_id,
                "payer": {
                    "email": email
                }
            }

            # Criação do pagamento no Mercado Pago
            payment_response = sdk.payment().create(pagamento_data)
            payment_status = payment_response.get("status")
            payment_body = payment_response.get("response")

            if payment_status == 201:  # Pagamento aprovado
                return JsonResponse({"status": "success", "payment": payment_body}, status=201)
            else:
                error_message = payment_body.get("message", "Erro desconhecido.")
                return JsonResponse({"status": "failure", "message": error_message}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"status": "failure", "message": "Erro ao processar os dados JSON."}, status=400)
        except Exception as e:
            return JsonResponse({"status": "failure", "message": f"Erro interno: {str(e)}"}, status=500)

    # Renderiza o template no caso de GET
    context = {
        "total": carrinho.total
    }
    return render(request, "pagamento/pagamento.html", context)

