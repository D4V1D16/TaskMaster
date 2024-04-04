from django.urls import path
from django.urls import include,path
from . import views

urlpatterns = [
    path("", views.inicio_sesion, name="InicioSesion"),
    path("CrearUsuario",views.crear_usuario, name='CrearUsuario'),
    path('EliminarUsuario', views.borrar_usuario, name='borrar_usuario'),
    path("Perfil", views.mostrar_usuario, name="Perfil")
]