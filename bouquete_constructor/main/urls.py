from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('cart', views.about, name='cart'),
    path('checkout', views.about, name='checkout'),
    path('payments', views.about, name='payments'),
    path('contacts', views.about, name='contacts'),
    path('help', views.about, name='help'),
    path('login', views.about, name='login'),
    path('status', views.about, name='status'),
]