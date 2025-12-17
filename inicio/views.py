from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Perro
from inicio.forms import ComprarPerro, BuscarPerro
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')


def otra(request):
    return render(request, 'otra.html')

@login_required
def comprar_perro(request, raza=None, tamaño=None):
    perro = None
    if request.method == 'POST':
        formulario = ComprarPerro(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data

            perro = Perro(raza=info.get("raza"), tamaño=info.get("tamaño"))
            perro.save()
            return redirect('listar')
    else:
        formulario = ComprarPerro()

    return render(request, 'comprar_perro.html', {'perros_comprados': perro, "formulario": formulario})


def listar_perros(request):
    formulario = BuscarPerro(request.GET)
    listado_de_perros = Perro.objects.all()

    if formulario.is_valid():
        raza_a_buscar = formulario.cleaned_data.get('raza')
        if raza_a_buscar:
            listado_de_perros = listado_de_perros.filter(raza__icontains=raza_a_buscar)

    return render(
        request,
        'listar_perros.html',
        {
            'listado_de_perros': listado_de_perros,
            'formulario': formulario
        }
    )


def ver_perro(request, perro_id):

    perro = Perro.objects.get(id=perro_id)

    return render(request, 'ver_perro.html', {'perro': perro})

def actualizar_perro(request, perro_id):

    perro = Perro.objects.get(id=perro_id)

    if request.method == 'POST':
        formulario = ComprarPerro(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data

            perro.raza = info.get("raza")
            perro.tamaño = info.get("tamaño")
            perro.save()
            return redirect('listar')
    else:
        formulario = ComprarPerro(initial={'raza': perro.raza, 'tamaño': perro.tamaño})

    return render(request, 'actualizar_perro.html', {'formulario': formulario, 'perro_id': perro_id})

class ActualizarPerro(LoginRequiredMixin, UpdateView):
    model = Perro
    template_name = 'actualizar_perro.html'
    #fields = ['raza', 'tamaño']
    fields = '__all__' # para que aparezcan todos los campos del modelo
    success_url = reverse_lazy('listar')

class EliminarPerro(LoginRequiredMixin, DeleteView):
    model = Perro
    template_name = 'eliminar_perro.html'
    fields = '__all__' # para que aparezcan todos los campos del modelo
    success_url = reverse_lazy('listar')