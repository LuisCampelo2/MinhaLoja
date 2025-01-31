from django.shortcuts import render
from django.urls import reverse
from users.forms import RegisterUser,CustomAuthenticationForm
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    form = CustomAuthenticationForm(request)
    form_action=reverse('authentication:login')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home:index')
            
        
    context = {
        'form': form,
        'form_action': form_action
    }
    return render(request,'authentication/pages/login.html',context)

def createAccount(request):
    form_action=reverse('authentication:create_account')
    form=RegisterUser()
    
    if request.method=='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Cria o usuário sem salvar diretamente.
            user.set_password(form.cleaned_data['password1'])  # Define a senha corretamente.
            user.save()  # Salva o usuário no banco.
            auth.login(request, user)  # Faz o login automático.
            return redirect('home:index')  
        else:
            form = RegisterUser()
        
    context = {
        'form': form,
        'form_action': form_action
    }
    return render(request,'authentication/pages/create_account.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect ('home:index')


