from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *



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