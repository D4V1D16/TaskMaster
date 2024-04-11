from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("CrearUsuario",views.crear_usuario, name='CrearUsuario'),
    path("EliminarUsuario", views.borrar_usuario, name='BorrarUsuario'),
    path("Data",views.obtener_datos_usuario, name="Data"),
]