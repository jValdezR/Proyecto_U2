from django.test import TestCase
from .models import *
import datetime
# Create your tests here.

# UsuarioTestCase es una clase de TestCase para guardar y leer objectos en la base de datos para la tabla Usuario, esto con el fin de corroborar que la informacion que se esta guardando sea correcta, integra, 
# responda las llaves foráneas y demás restricciones.

class UsuarioTestCase(TestCase):
  # Guarda en la bd
  def setUp(self):
    Usuario.objects.create(username='testuser', password='123456789!', edad=23, telefono='1234567890')
  # Lee desde la bd
  def testUsuario(self):
    usr = Usuario.objects.all()

# DeveloperTestCase es una clase de TestCase para guardar y leer objectos en la base de datos para la tabla Developer, esto con el fin de corroborar que la informacion que se esta guardando sea correcta, integra, 
# responda las llaves foráneas y demás restricciones.

class DeveloperTestCase(TestCase):
  # Guarda en la bd
  def setUp(self):
    Developer.objects.create(id_developer=Usuario(email="jdv_rodriguez@hotmail.com"),name='ValRomSoft',description='Testing', date=datetime.datetime.now())
  # Lee desde la bd
  def testDeveloper(self):
    JValdez = Developer.objects.all()

# AppTestCase es una clase de TestCase para guardar y leer objectos en la base de datos para la tabla Developer, esto con el fin de corroborar que la informacion que se esta guardando sea correcta, integra, 
# responda las llaves foráneas y demás restricciones.

class AppTestCase(TestCase):
  # Guarda en la bd
  def setUp(self):
    App.objects.create(authorApp=Developer(id_developer=Usuario(email="jdv_rodriguez@hotmail.com")),title='App test',description='Testing', date=datetime.datetime.now())
  # Lee desde la bd
  def testApp(self):
    app = App.objects.all()

# CommentTestCase es una clase de TestCase para guardar y leer objectos en la base de datos para la tabla Developer, esto con el fin de corroborar que la informacion que se esta guardando sea correcta, integra, 
# responda las llaves foráneas y demás restricciones.

class CommentTestCase(TestCase):
  # Guarda en la bd
  def setUp(self):
    Comment.objects.create(authorComment=Usuario(email="jdv_rodriguez@outlook.com"),id_app=App(pk=1),title='testing comment',stars= 'Excelente',comment='Testing', date=datetime.datetime.now())
  # Lee desde la bd
  def testComment(self):
    cmt = Comment.objects.all()