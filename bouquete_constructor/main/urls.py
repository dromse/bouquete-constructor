from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('payments', views.payments, name='payments'),
    path('contacts', views.contacts, name='contacts'),
    path('help', views.help, name='help'),
    path('login', views.login, name='login'),
    path('status', views.status, name='status'),
]