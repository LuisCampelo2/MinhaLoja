from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import MyAccountForm,EditMyAccountForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def myaccount(request):
    user=request.user
    form=MyAccountForm(instance=user)

    context={
        'form':form
    }
    return render(request,'users/pages/myaccount.html',context)


@login_required
def editdata(request):
    user = request.user
    
    if request.method == 'POST':
        form = EditMyAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:myaccount')
    else:
        form = EditMyAccountForm(instance=user)
    context = {
        'form': form,
        'form_action': reverse('users:alterdata'),
    }
    return render(request, 'users/pages/alterdata.html', context)
