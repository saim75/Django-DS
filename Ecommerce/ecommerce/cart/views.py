from django.shortcuts import render
from .cart import Cart

# Create your views here.
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return render(request, 'cart/menucart.html', {'cart': cart})
