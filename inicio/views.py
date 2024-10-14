from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render

def inicio(request):
    return HttpResponse ('Inicio')

def home(request):
    return HttpResponse ('Bienvenido') 

def ropa_nueva(request):
    return HttpResponse ('Cargar nueva indumentaria')

def primer_template(request):
    
    fecha_actual = datetime.now()
    datos = {'fecha_actual': fecha_actual}
    
    # v1
    # with open(r'inicio\templates\primer_template.html') as archivo_template:
    #     template = Template(archivo_template.read())
    # contexto = Context(datos)
    # render_template = template.render(contexto)
    # return HttpResponse(render_template)
    
    # v2
    # template = loader.get_template('primer_template.html')
    # contexto = Context(datos)
    # render_template = template.render(datos)
    # return HttpResponse(render_template)

    
    return render(request, 'primer_template')

