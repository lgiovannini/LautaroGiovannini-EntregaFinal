from django.urls import path
from blog.views import (
    inicio, 
    home, 
    nueva_ropa, 
    buscar_ropa, 
    about, 
    ver_ropa, 
    eliminar_ropa, 
    editar_ropa)

app_name = 'blog'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('nueva-ropa/', nueva_ropa, name='nueva_ropa'),
    path('buscar-ropa/', buscar_ropa, name='buscar_ropa'),
    path('ver-ropa/<int:id>/', ver_ropa, name='ver_ropa'),
    path('eliminar-ropa/<int:id>/', eliminar_ropa, name='eliminar_ropa'),
    path('editar-ropa/<int:id>/', editar_ropa, name='editar_ropa'),
    
    ]
