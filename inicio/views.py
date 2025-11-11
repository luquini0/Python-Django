from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Perro

# Create your views here.

def inicio(request):
    """ return HttpResponse("Hello, world. You're at the polls index.") """
    return render(request, 'inicio.html')


def otra(request):
    return render(request, 'otra.html')


def comprar_perro(request, raza, tamaño):

    perro = Perro(raza=raza, tamaño=tamaño)
    perro.save()

    return render(request, 'comprar_perro.html', {'perros_comprados': perro})

def listar_perros(request):

    perros = Perro.objects.all()

    return render(request, 'listar_perros.html', {'listado_de_perros': perros})