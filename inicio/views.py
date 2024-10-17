from django.http import HttpResponse
from django.shortcuts import render, redirect
from inicio.models import Ropa
from inicio.forms import CrearRopaForm, BuscarRopaForm

def inicio(request):
    return HttpResponse ('Blank')

def home(request):
    return render(request, 'inicio/index.html')

def about(request):
    return render(request, 'inicio/about.html')


def nueva_ropa(request):
    
    formulario = CrearRopaForm()
    
    if request.method == 'POST':
        formulario = CrearRopaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            ropa = Ropa(type=data.get('type'), brand=data.get('brand'), size=data.get('size'))
            ropa.save()
            return redirect('inicio:buscar_ropa')

    
    return render(request, 'inicio/nueva_ropa.html', {'form': formulario})

def buscar_ropa(request):
    
    formulario = BuscarRopaForm(request.GET)
    if formulario.is_valid():
        type = formulario.cleaned_data.get('type')
        ropas = Ropa.objects.filter(type__icontains=type)
        
    return render(request, 'inicio/buscar_ropa.html', {'ropas': ropas, 'form' : formulario})