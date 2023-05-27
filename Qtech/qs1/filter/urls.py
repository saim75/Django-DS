from django.urls import path
from . import views

urlpatterns = [
    
    path('categories/', views.category, name='category_page'),
    path('brands/', views.brand, name='brand_page'),
    path('warranties/', views.warranty, name='warranty_page'),
    path('sellers/', views.seller, name='seller_page'),
    path('products/', views.product, name='product_page'),
]
