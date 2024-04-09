from django.urls import path
from django.urls import include,path
from . import views

urlpatterns = [
    path("InicioSesion",views.inicio_sesion, name='InicioSesion'),
    path("CrearUsuario",views.crear_usuario, name='CrearUsuario'),
    path("EliminarUsuario", views.borrar_usuario, name='borrar_usuario'),
    path("Autenticacion", views.autenticar_usuario,name='Autenticacion'),
    path("data",views.obtener_datos_usuario, name="data"),
]