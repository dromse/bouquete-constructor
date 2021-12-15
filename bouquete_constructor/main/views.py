from django.shortcuts import render


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