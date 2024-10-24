from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Ropa
from blog.forms import CrearRopaForm, BuscarRopaForm, EditarRopaForm

def inicio(request):
    return HttpResponse ('Blank')

def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')


def nueva_ropa(request):
    
    formulario = CrearRopaForm()
    
    if request.method == 'POST':
        formulario = CrearRopaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            ropa = Ropa(type=data.get('type'), brand=data.get('brand'), size=data.get('size'))
            ropa.save()
            return redirect('blog:buscar_ropa')

    
    return render(request, 'blog/nueva_ropa.html', {'form': formulario})

def buscar_ropa(request):
    
    formulario = BuscarRopaForm(request.GET)
    if formulario.is_valid():
        type = formulario.cleaned_data.get('type')
        ropas = Ropa.objects.filter(type__icontains=type)
        
    return render(request, 'blog/buscar_ropa.html', {'ropas': ropas, 'form' : formulario})

def ver_ropa(request, id):
    ropa = Ropa.objects.get(id=id)
    return render(request, 'blog/ver_ropa.html', {'ropa': ropa})

def eliminar_ropa(request, id):
    ropa = Ropa.objects.get(id=id)
    ropa.delete()
    return redirect('blog:buscar_ropa')

def editar_ropa(request, id):
    ropa = Ropa.objects.get(id=id)
    
    formulario = EditarRopaForm(initial={'type': ropa.type, 'brand': ropa.brand, 'size': ropa.size})
    
    if request.method == "POST":
        formulario = EditarRopaForm(request.POST)
        if formulario.is_valid():
            ropa.type = formulario.cleaned_data.get('type')
            ropa.brand = formulario.cleaned_data.get('brand')
            ropa.size = formulario.cleaned_data.get('size')
            
            ropa.save()

            return redirect('blog:buscar_ropa')
    return render(request, 'blog/editar_ropa.html', {'ropa': ropa, 'form': formulario})