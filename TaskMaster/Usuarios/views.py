from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.authentication import TokenAuthentication
@api_view(('POST',))
def inicio_sesion(request):
    user = get_object_or_404(User,username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"error":"Invalid Password"}, status = status.HTTP_400_BAD_REQUEST)
    
    token, create= Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token": token.key,"user":serializer.data},status = status.HTTP_200_OK)

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
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(('GET',))
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def mostrar_usuario(request):
    userdata = {
        "username": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
    }

    print(userdata)


    return Response("You are login with {}".format(request.user),status = status.HTTP_200_OK)


@api_view(('DELETE',))
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def borrar_usuario(request):
    usuario = get_object_or_404(User,id=request.user.id)
    usuario.delete()
    return Response("Se ha eliminado correctamente el usuario",status=status.HTTP_200_OK)


