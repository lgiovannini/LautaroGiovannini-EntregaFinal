from django.urls import path
from inicio.views import inicio, home, ropa_nueva, primer_template

urlpatterns = [
    path('', inicio),
    path('home/', home),
    path('ropa-nueva/', ropa_nueva),
    path('primer-template/', primer_template)
    ]
