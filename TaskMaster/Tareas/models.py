from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    idTarea = models.AutoField(primary_key=True)
    nombreTarea = models.CharField(max_length=30)
    descripcion = models.TextField()
    usuarioAsignado = models.ForeignKey(User, on_delete=models.CASCADE)
    fechaComienzo = models.DateField(auto_now_add=True)
    fechaVencimiento = models.DateTimeField()


