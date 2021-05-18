from django.shortcuts import render
from django.http import HttpResponse
from.models import Product

def index(request):
    products=Product.objects.all()
    parameter={'product' : products}
    return render(request, 'shop/index.html', parameter)
def about(request):
    return render(request, 'shop/about.html')
def crowns(request):
    products = Product.objects.all()
    parameter={'product' : products}
    return render(request, 'shop/crowns.html', parameter)
def masks(request):
    products = Product.objects.all()
    parameter={'product' : products}
    return render(request, 'shop/masks.html', parameter)
def stones(request):
    products = Product.objects.all()
    parameter={'product' : products}
    return render(request, 'shop/stones.html', parameter)
def suits(request):
    products = Product.objects.all()
    parameter={'product' : products}
    return render(request, 'shop/suits.html', parameter)
def weapons(request):
    products = Product.objects.all()
    parameter={'product' : products}
    return render(request, 'shop/weapons.html', parameter)
def thanks(request):
    return render(request, 'shop/thanks.html')
