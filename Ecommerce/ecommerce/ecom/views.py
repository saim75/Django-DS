from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.db.models import Q
from product.models import Product, Category
from .forms import SignUpForm

# Create your views here.
def index(request):
    products = Product.objects.all()[:8]
    return render(request, 'ecom/front.html',{'products':products})

def signup(request):
    if request.method =='post':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=password)
            #login(request, user)
            return redirect('ecom:login')
        else:
            form = SignUpForm()
    return render(request, 'ecom/signup.html')


def login(request):
    return render(request, 'ecom/login.html')


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    active_category = request.GET.get('category')
    if active_category:
        products = products.filter(category__slug=active_category)
    query = request.GET.get('q','')
    
    if query:
        products = products.filter(
            Q(name__icontains=query)|
            Q(description__icontains=query)|
            Q(price__icontains=query)|
            Q(category__name__icontains=query)
        ).distinct()
    
    context = {
        'categories':categories,
        'products':products,
        'active_category':active_category
    }
    return render(request, 'ecom/shop.html',{'products':products})

