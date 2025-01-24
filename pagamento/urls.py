# urls.py
from django.urls import path
from . import views
app_name='pagamento'

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
]