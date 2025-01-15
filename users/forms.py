from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from users.models import CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Nome de usuário ou Email",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome de usuário ou email'
        }),
    )
    password = forms.CharField(
        label="Senha",
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        }),
    )

    def clean(self):
        """
        Verifica se as credenciais fornecidas são válidas.
        """
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username_or_email and password:
            user = authenticate(username=username_or_email, password=password)
            if not user:
                # Verifica se o email foi usado como nome de usuário
                try:
                    user = CustomUser.objects.get(email=username_or_email)
                    user = authenticate(username=user.username, password=password)
                except CustomUser.DoesNotExist:
                    user = None

            if not user:
                raise ValidationError("Credenciais inválidas. Verifique os dados inseridos.")
            if not user.is_active:
                raise ValidationError("Esta conta está desativada.")
        
        return super().clean()


class RegisterUser(forms.ModelForm):
    first_name = forms.CharField(
        label=" Nome:",
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        label="Sobrenome:",
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        label="Email:"
    )
    username = forms.CharField(
        label="Nome de Usuário:",
        required=True,
    )
    password1 = forms.CharField(
        label="Senha:",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        }),
    )
    password2 = forms.CharField(
        label="Repita sua senha:",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }),
    )
    cpf = forms.CharField(
        max_length=11,
        label='CPF',
        help_text='Insira o CPF com 11 dígitos numéricos',
    )
    telefone = forms.CharField(
        max_length=15,
        required=False,
        label='Telefone',
        help_text='Insira o telefone no formato (XX) XXXXX-XXXX',
    )
    data_nascimento = forms.DateField(
        required=False,
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={
            'type': 'date',  # Adiciona o seletor de data
            'class': 'form-control',  # Classe CSS para estilo
    }),
)   
    GENERO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
    ('N', 'Prefiro não informar'),
]

    genero = forms.ChoiceField(
        choices=GENERO_CHOICES,
        required=True,
        label="Gênero",
        widget=forms.Select(attrs={
        'class': 'form-control',  # Classe CSS para estilização
    }),
)


    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2', 'cpf', 'data_nascimento',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Este email já está registrado.', code='invalid')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('Este nome de usuário já está em uso.', code='invalid')
        return username

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if CustomUser.objects.filter(cpf=cpf).exists():
            raise ValidationError('Este CPF já está registrado.', code='invalid')
        return cpf

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('As senhas não coincidem.')
        return password2

class MyAccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'email',
            'username','cpf', 'data_nascimento','telefone'
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tornar todos os campos somente leitura
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True

class EditMyAccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'email',
            'username','telefone'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Este email já está registrado.', code='invalid')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('Este nome de usuário já está em uso.', code='invalid')
        return username