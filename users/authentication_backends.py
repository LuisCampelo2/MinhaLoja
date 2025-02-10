from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
import re
from django.core.exceptions import ValidationError
 
User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Tenta encontrar o usuário pelo e-mail
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                # Se não encontrar por e-mail, tenta pelo nome de usuário
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        # Verifica a senha
        if user.check_password(password):
            return user
        return None



def validar_cpf(cpf):
    cpf = re.sub(r"[^0-9]", "", cpf)  # Remove caracteres não numéricos

    if len(cpf) != 11 or cpf in (str(i) * 11 for i in range(10)):  # Verifica sequência repetida
        raise ValidationError("CPF inválido.")

    # Cálculo dos dígitos verificadores
    def calcular_digito(cpf, peso):
        soma = sum(int(digit) * peso for digit, peso in zip(cpf, range(peso, 1, -1)))
        resto = (soma * 10) % 11
        return str(resto if resto < 10 else 0)

    if calcular_digito(cpf[:9], 10) != cpf[9] or calcular_digito(cpf[:10], 11) != cpf[10]:
        raise ValidationError("CPF inválido.")
