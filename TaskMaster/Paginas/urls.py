from django.urls import path
from django.urls import include,path
from . import views

urlpatterns = [
        path("", views.frontIniciarSesion, name='Log-In'),
        path("Sign-In", views.frontCrearUsuario, name="Sign-In"),
        path("Home", views.home, name='Home'),
]