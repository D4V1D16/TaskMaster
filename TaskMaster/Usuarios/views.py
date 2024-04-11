from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


#Crear Usuario
@api_view(('POST',))
def crear_usuario(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        username = serializer.validated_data['username']
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Ya existe un usuario con ese nombre de usuario.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        
        user.save()

        return Response({"user": serializer.data}, status = status.HTTP_201_CREATED)
    else:
        print("Se produjo un error al crear un usuario")
        print(serializer.errors)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




#Borrar Usuario
@api_view(('DELETE',))
def borrar_usuario(request):
    usuario = get_object_or_404(User,id=request.user.id)
    usuario.delete()
    return Response("Se ha eliminado correctamente el usuario",status=status.HTTP_200_OK)

@api_view(['GET'])
def obtener_datos_usuario(request):  
    permission_classes = [IsAuthenticated]
    usuario = request.user
    datos_usuario = {
        'username': usuario.username,
        'email': usuario.email,
    }
    return Response({'status': 'success', 'datos_usuario': datos_usuario})
    