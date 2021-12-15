from django.urls import path
from . import views
from .views import CartView


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('cart', CartView.as_view(), name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('payments', views.payments, name='payments'),
    path('contacts', views.contacts, name='contacts'),
    path('help', views.help, name='help'),
    path('login', views.login, name='login'),
    path('status', views.status, name='status'),
    path('constructor', views.constructor, name='constructor'),
    path('flowers', views.flowers, name='flowers'),
]