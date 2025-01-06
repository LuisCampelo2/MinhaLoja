from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Usuário ou E-mail")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput) 

    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username_or_email and password:
            # Autenticar por e-mail ou usuário
            user = authenticate(username=username_or_email, password=password)
            if user is None:
                from django.contrib.auth.models import User

                try:
                    # Verifica se é um e-mail e tenta buscar o usuário
                    user_by_email = User.objects.get(email=username_or_email)
                    user = authenticate(username=user_by_email.username, password=password)
                except User.DoesNotExist:
                    pass

            if user is None:
                raise forms.ValidationError("Credenciais inválidas. Verifique o nome de usuário/e-mail e a senha.")
            else:
                self.confirm_login_allowed(user)

        return self.cleaned_data
    
    
class RegisterUser(UserCreationForm):
    first_name = forms.CharField(
        label="Primeiro nome:",
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        label="Sobrenome:",
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        label="email:"
    )

    username=forms.CharField(
        label="Nome de Usuario:",
        required=True,
    )
    
    password1 = forms.CharField(
        label="Senha:",
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',  # Classe CSS (opcional)
        'placeholder': 'Digite sua senha'  # Placeholder (opcional)
    }),
)
    password2 = forms.CharField(
        label="Repita sua senha:",
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',  # Classe CSS (opcional)
    }),
)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Verifica se o e-mail já está em uso
        if User.objects.filter(email=email).exists():
            raise ValidationError('Já existe este e-mail.', code='invalid')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # Verifica se o nome de usuário já está em uso
        if User.objects.filter(username=username).exists():
            raise ValidationError('Este nome de usuário já está em uso.', code='invalid')
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        # Verifica se a senha tem pelo menos 8 caracteres
        if len(password1) < 8:
            raise ValidationError('A senha deve ter pelo menos 8 caracteres.')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # Verifica se as senhas coincidem
        if password1 != password2:
            raise ValidationError('As senhas não coincidem.')
        return password2