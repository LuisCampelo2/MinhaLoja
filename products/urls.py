from django.contrib import admin
from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('produtos/<int:id>/',views.produto_view,name='produto_view')
    
]