from .import views
from django.urls import path

urlpatterns = [

    path('goods/', views.product, name='product'),

]



