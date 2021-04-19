from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import *

class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ['email', 'username', 'edad','telefono', 'is_staff',]

admin.site.register(Usuario, UsuarioAdmin)

admin.site.register(App)

admin.site.register(Developer)

admin.site.register(Comment)