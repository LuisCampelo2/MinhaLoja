# urls.py
from django.urls import path
from . import views
app_name='pagamento'

urlpatterns = [
    path('create-payment/', views.create_payment, name='create_payment'),
    path('checkout/', views.checkout, name='checkout'),
]