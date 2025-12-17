from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from usuarios.forms import FormularioRegistro

def login_view(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            auth_login(request, usuario)
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()

    return render(request, 'login.html', {'formulario': formulario})


def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')

    return render(request, 'logout.html')


def register(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST) 
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = FormularioRegistro()

    return render(request, 'register.html', {'formulario': formulario})
