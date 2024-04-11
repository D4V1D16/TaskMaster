from django.urls import path, include
from rest_framework import routers
from .api import TareasViewSet

router = routers.DefaultRouter()

router.register('Tareas',TareasViewSet,'Tareas')

urlpatterns = [
    path('',include(router.urls)),
]