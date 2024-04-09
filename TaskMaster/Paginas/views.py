from django.shortcuts import render
from . forms import crearUsuario,inicioSesion

# Create your views here.

def home(request):
  
    return render(request, 'home.html')
  
def frontCrearUsuario(request):
    return render(request, 'createAccount.html',{
        'form': crearUsuario
    })

def frontIniciarSesion(request):
    return render(request,'Login.html',{
        'form':inicioSesion
    })
