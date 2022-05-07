from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from .models import (Flower, Cart, Customer)


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html') 


def cart(request):
    return render(request, 'main/cart.html') 


def checkout(request):
    return render(request, 'main/checkout.html') 


def payments(request):
    return render(request, 'main/payments.html') 


def contacts(request):
    return render(request, 'main/contacts.html') 


def help(request):
    return render(request, 'main/help.html') 


def status(request):
    return render(request, 'main/status.html')


def login(request):
    return render(request, 'main/help.html')


def constructor(request):
    return render(request, 'main/constructor.html')


def flowers(request):
    flowers_list = Flower.objects.all()
    return render(request, 'main/flowers.html', {'flowers': flowers_list})


class CartView(View):
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        cart = Cart.objects.get(owner=customer)

        context = {
            'cart': cart,
        }

        return render(request, 'main/cart.html', context)


class AddToCartView(View):

    def get(self, request, *args, **kwargs):
        
        return HttpResponseRedirect('/cart/')