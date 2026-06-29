from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'scoop_app/home.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'scoop_app/products.html', {'products': products})

def about(request):
    return render(request, 'scoop_app/about.html')

def contact(request):
    return render(request, 'scoop_app/contact.html')