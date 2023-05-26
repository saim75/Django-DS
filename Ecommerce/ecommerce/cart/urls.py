from django.urls import path

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]