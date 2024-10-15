from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from django.shortcuts import render
from inicio.models import Ropa

def inicio(request):
    return HttpResponse ('Blank')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def buscar_ropa(request):
    return render(request, 'buscar_ropa.html')

def ropa_nueva(request):
    return render(request, 'ropa_nueva.html', {})


