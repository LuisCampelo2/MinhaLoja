from django.shortcuts import render
from django.urls import reverse
from .forms import RegisterUser
from django.contrib import auth
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'loja/pages/index.html')

def createAccount(request):
    form_action=reverse('loja:create_account')
    form=RegisterUser()
    
    if request.method=='POST':
        form=RegisterUser(request.POST)
        user = form.save(commit=False)  # Cria o usuário sem salvar diretamente.
        user.set_password(form.cleaned_data['password1'])  # Define a senha corretamente.
        user.save()  # Salva o usuário no banco.
        auth.login(request, user)  # Faz o login automático.
        return redirect('home:index')  
            
        
    context = {
        'form': form,
        'form_action': form_action
    }
    return render(request,'loja/pages/create_account.html',context)