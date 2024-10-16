from django.http import HttpResponse
from django.shortcuts import render
from inicio.models import Ropa

def inicio(request):
    return HttpResponse ('Blank')

def home(request):
    return render(request, 'inicio/index.html')

def about(request):
    return render(request, 'inicio/about.html')

def nueva_ropa(request):
    
    print('Request', request)
    print('POST', request.POST)
    
    ropa = Ropa(request.POST.get('type'), request.POST.get('brand'), request.POST.get('size'))
    ropa.save()

    return render(request, 'inicio/nueva_ropa.html', {'ropa': ''})

def buscar_ropa(request):
    return render(request, 'inicio/buscar_ropa.html', {'ropa': ''})
