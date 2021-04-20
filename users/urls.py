from django.urls import path
from .views import RegisterView

urlpatterns = [
    # redirecciona al registro
    path('register/', RegisterView.as_view(), name='register'),
]