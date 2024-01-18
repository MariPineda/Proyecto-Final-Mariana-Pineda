from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SociosFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    socio = forms.IntegerField()
    activo = forms.BooleanField(required=False)

class LibrosFormulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    tipo = forms.CharField(max_length=60)
    edadRecomendada = forms.IntegerField()

class BusquedaSocios(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    socio = forms.IntegerField()
    activo = forms.BooleanField()

class UserRegistrationForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "last_name", "first_name"]


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingresar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "last_name", "first_name"]

class AvatarFormulario(forms.Form):
    image = forms.ImageField()