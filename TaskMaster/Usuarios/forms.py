from django import forms

class inicioSesion(forms.Form):
    usuario = forms.CharField(max_length=100,label=False, widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    contrasena = forms.CharField(max_length=100,label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

class crearUsuario(forms.Form):
    usuario = forms.CharField(max_length=30,label=False, widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    contrasena = forms.CharField(max_length=30,label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    email = forms.CharField(max_length=50,label=False, widget=forms.EmailInput(attrs={'placeholder': 'correo'}))
    fname = forms.CharField(max_length=30,label=False, widget=forms.TextInput(attrs={'placeholder': 'Primer Nombre'}))
    lname = forms.CharField(max_length=30,label=False, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))