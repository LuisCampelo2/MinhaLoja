from django.contrib import admin
from django.urls import path
from . import views

app_name='home'

urlpatterns = [
     path('',views.index,name='index'),
     path('search/', views.search_view, name='search'),
     path('busca',views.search_view,name='busca'),
]