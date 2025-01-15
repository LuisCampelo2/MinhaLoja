from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import MyAccountForm,EditMyAccountForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
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
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    form = EditMyAccountForm(instance=user)
    context = {
        'form': form,
        'form_action': reverse('users:alterdata'),
    }
    return render(request, 'users/pages/alterdata.html', context)
