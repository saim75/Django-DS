from django.shortcuts import render
from .models import Category, Brand, Warranty, Seller, Product

# Create your views here.
def home(request):
    return render(request, 'temp/home.html')

def category(request):
    categories = Category.objects.all()
    return render(request, 'temp/category.html', {'categories': categories})

def brand(request):
    brands = Brand.objects.all()
    return render(request, 'temp/brand.html', {'brands': brands})

def warranty(request):
    warranties = Warranty.objects.all()
    return render(request, 'temp/warranty.html', {'warranties': warranties})

def seller(request):
    sellers = Seller.objects.all()
    return render(request, 'temp/seller.html', {'sellers': sellers})

def product(request):
    products = Product.objects.all()
    return render(request, 'temp/product.html', {'products': products})
