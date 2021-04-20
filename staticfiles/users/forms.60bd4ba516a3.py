from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario, App

# Formulario para desplegar los campos extras
class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('email','edad','telefono')
#Formulario que permite la edicion de un usuario
class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = UserChangeForm.Meta.fields
        