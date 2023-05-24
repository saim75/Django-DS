from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()[:8]
    return render(request, 'ecom/front.html',{'products':products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'ecom/shop.html',{'products':products})

