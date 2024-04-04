from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ('idTarea','nombreTarea','descripcion','usuarioAsignado','fechaVencimiento')
        read_only_fields = ('fechaComienzo',)