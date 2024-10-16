from django.urls import path
from inicio.views import inicio, home, nueva_ropa, buscar_ropa, about

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('home/', home, name='home'),
    path('nueva-ropa/', nueva_ropa, name='nueva_ropa'),
    path('buscar-ropa/', buscar_ropa, name='buscar_ropa'),
    path('about/', about, name='about')
    ]
