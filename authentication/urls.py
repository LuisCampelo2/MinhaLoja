from django.contrib import admin
from django.urls import path
from . import views

app_name='authentication'

urlpatterns = [
    path('create-account/',views.createAccount,name='create_account'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    
]