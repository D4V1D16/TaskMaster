from django.shortcuts import get_object_or_404
from .forms import *
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
#Iniciar Sesion
@api_view(('POST',))
def inicio_sesion(request):
    user = get_object_or_404(User,username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail":"El usuario o la Contraseña podrian estar incorrectas"}, status = status.HTTP_400_BAD_REQUEST)
    
    token, created= Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token": token.key,"user":serializer.data},status = status.HTTP_200_OK)

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

        token = Token.objects.create(user = user)

        return Response({'token': token.key, "user": serializer.data}, status = status.HTTP_201_CREATED)
    else:
        print("Se produjo un error al crear un usuario")
        print(serializer.errors)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#Autenticar Usuario con el Token como Header
@api_view(('GET',))
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def autenticar_usuario(request):
    return Response("Passed for {}".format(request.user.username))


#Borrar Usuario
@api_view(('DELETE',))
@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
def borrar_usuario(request):
    usuario = get_object_or_404(User,id=request.user.id)
    usuario.delete()
    return Response("Se ha eliminado correctamente el usuario",status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def obtener_datos_usuario(request):
    usuario = request.user
    datos_usuario = {
        'username': usuario.username,
        'email': usuario.email,
    }
    return Response(datos_usuario)

