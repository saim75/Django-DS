from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
from  django.contrib.auth import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.LogoutView.as_View(), name='logout'),
    path('login/', views.login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)