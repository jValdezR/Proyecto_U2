from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UsuarioCreationForm

class RegistrarView(CreateView):
    form_class = UsuarioCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registrar.html'