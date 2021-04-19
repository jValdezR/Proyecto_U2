from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

# El modelo User será la tabla que almacene la informacion de los usuarios, agregando campos extra para complementar su informacion.
class Usuario(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    telefono = models.CharField(default="", max_length=10)
    imagen = models.ImageField(default="", null=True, blank=True)
    rol = models.CharField(default="default", max_length=255)
# El modelo Developer será la tabla que almacene la informacion de las empresas o usuarios desarrolladores, la cual esta'ra ligada al usuario que la haya creado.
class Developer(models.Model):
  id_developer = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
  name = models.CharField(max_length=255, default="")
  description = models.TextField(max_length=255)
  date = models.DateTimeField(auto_now_add=True)
# El modelo App será la tabla que almacene la informacion de una aplicacion desarrollada por un Developer.
class App(models.Model):
  authorApp = models.ForeignKey(Developer, on_delete=models.CASCADE)
  title = models.CharField(default="", max_length=255)
  description = models.TextField(default="Sin descripcion")
  imageApp = models.ImageField(default="", null=True, blank=True)
  date = models.DateTimeField(auto_now_add=True)

# El modelo Comment será la tabla que almacene los comentarios de los usuarios a las aplicaciones posteadas.
class Comment(models.Model):
  _0 = 'Muy mala'
  _1 = 'Puede_mejorar'
  _2 = 'Usable'
  _3 = 'Buena'
  _4 = 'Excelente'
  opinion = [
      (_0, 'Muy mala'),
      (_1, 'Puede mejorar'),
      (_2, 'Usable'),
      (_3, 'Buena'),
      (_4, 'Excelente'),
    ]
  authorComment = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
  id_app = models.ForeignKey(App, on_delete=models.CASCADE)
  title = models.CharField(max_length=255, default="")
  stars = models.CharField(max_length=255, choices=opinion, default=_4)
  comment = models.TextField(default="Sin descripcion")
  date = models.DateTimeField(auto_now_add=True)