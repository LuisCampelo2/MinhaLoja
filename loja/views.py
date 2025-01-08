from django.shortcuts import render
from django.urls import reverse
from .forms import RegisterUser,AuthenticationForm
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, 'loja/pages/index.html')

def login_view(request):
    form = AuthenticationForm(request)
    form_action=reverse('loja:login')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('loja:index')
            
        
    context = {
        'form': form,
        'form_action': form_action
    }
    return render(request,'loja/pages/login.html',context)

def createAccount(request):
    form_action=reverse('loja:create_account')
    form=RegisterUser()
    
    if request.method=='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Cria o usuário sem salvar diretamente.
            user.set_password(form.cleaned_data['password1'])  # Define a senha corretamente.
            user.save()  # Salva o usuário no banco.
            auth.login(request, user)  # Faz o login automático.
            return redirect('loja:index')  
        else:
            form = RegisterUser()
        
    context = {
        'form': form,
        'form_action': form_action
    }
    return render(request,'loja/pages/create_account.html',context)

def logout_view(request):
    logout(request)
    return redirect ('loja:index')


