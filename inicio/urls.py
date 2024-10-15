from django.urls import path
from inicio.views import inicio, home, ropa_nueva, buscar_ropa, about

urlpatterns = [
    path('', inicio, name='inicio'),
    path('home/', home, name='home'),
    path('ropa-nueva/', ropa_nueva, name='ropa_nueva'),
    path('buscar-ropa/', buscar_ropa, name='buscar_ropa'),
    path('about/', about, name='about')
    ]
