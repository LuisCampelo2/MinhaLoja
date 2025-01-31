"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from pagamento import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('home.urls')),
    path('authentication/',include('authentication.urls')),
    path('products/',include('products.urls')),
    path('users/',include('users.urls')),
    path('orders/', include('orders.urls')),
    path('pagamento/',include('pagamento.urls')),
    path('admin/', admin.site.urls),
    path('create_payment/', views.create_payment_card, name='create_payment_card'),
    path('crete_paymente_pix/',views.create_pix_payment,name='create_payment_pix'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

