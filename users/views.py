from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import MyAccountForm,EditMyAccountForm

# Create your views here.
def myaccount(request):
    user=request.user
    form=MyAccountForm(instance=user)

    context={
        'form':form
    }
    return render(request,'users/pages/myaccount.html',context)

def editdata(request):
    user = request.user
    form_action = reverse('users:alterdata')  # Gera a URL para o formulário

    if request.method == 'POST':  # Corrigido para verificar o método da requisição
        form = EditMyAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:myaccount')  # Redireciona após salvar
    else:
        form = EditMyAccountForm(instance=user)  # Para requisições GET, carrega o formulário com dados do usuário

    context = {
        'form': form,
        'form_action': form_action,
    }
    return render(request, 'users/pages/alterdata.html', context)