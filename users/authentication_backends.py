from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

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

 