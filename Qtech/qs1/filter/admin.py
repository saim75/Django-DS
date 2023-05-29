from django.contrib import admin
from .models import Category, Brand, Warranty, Seller, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
   

@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'warranty', 'seller', 'price']
    list_filter = ['category', 'brand', 'warranty', 'seller']
    search_fields = ['name', 'category__name', 'brand__name', 'warranty__name', 'seller__name']
    
    def get_ordering(self, request):
        return ['name']