from django.contrib import admin
from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('minhaconta/',views.myaccount,name='myaccount'),
    path('editardados/',views.editdata,name='alterdata'),
]