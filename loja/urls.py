from django.contrib import admin
from django.urls import path
from . import views

app_name='loja'

urlpatterns = [
    path('',views.index,name='index'),
    path('create_account/',views.createAccount,name='create_account'),
    path('login/',views.login,name='login'),
]