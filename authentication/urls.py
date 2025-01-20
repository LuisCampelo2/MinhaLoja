from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='authentication'

urlpatterns = [
    path('create-account/',views.createAccount,name='create_account'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    
    path("reset-password/",auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='esqueci_senha')
    
]