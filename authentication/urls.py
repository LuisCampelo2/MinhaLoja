from django.contrib import admin
from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name='authentication'

urlpatterns = [
    path('create-account/',views.createAccount,name='create_account'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    
    path("reset-password/", auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        success_url=reverse_lazy('authentication:password_reset_done')  
    ), name='esqueci_senha'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',
    success_url=reverse_lazy('authentication:password_reset_complete')
    ), name='password_reset_confirm'),
     path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]