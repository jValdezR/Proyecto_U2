from django.urls import path
from .views import RegistrarView

urlpatterns = [
    path('registrar/', RegistrarView.as_view(), name='registrar'),
]