from django.views.generic import TemplateView
from django.shortcuts import render
from users.models import *
from django.http import HttpResponse,JsonResponse

# Direcciona al index
def index(request):
    return render(request,'index.html')
# Direcciona al home, enviando un objeto con todas las aplicaciones en la bd
def home(request):
    json = {
        "info" : App.objects.all()
    }
    return render(request,'home.html',context=json)
# Direcciona al modal de usuario, incluyendo un objeto con la informacion de todos los usuarios que será filtrado una vez llegue al html y compruebe con el usuario activo
def user(request):
    json = {
        "info" : Usuario.objects.all()
    }
    return render(request,'user.html', context=json)
# Drecciona a la pagina para editar las propiedades de un usuario, solo incluye la edad y telefono como campos editables.
def editUser(request,id):
    obj = Usuario.objects.get(id=id)
    json = {
        "edad" : obj.edad,
        "Telefono" : obj.telefono,
    }
    return render(request,'edituser.html',context=json)
# Esta funcion se encarga de recopilar los objetos enviados por el formulario de edituser y actualizar el objeto que le corresponda para despues guardar en la bd.
# Una vez completado lo anterior, redirecciona al modal de usuario.
def updateuser(request,id):
    obj = Usuario.objects.get(id=id)
    obj.edad = request.GET['edad']
    obj.telefono = request.GET['Telefono']
    obj.save()
    json = {
        "info" : Usuario.objects.all()
    }
    return render(request,'user.html',context=json)
# Direcciona a la pagina para cambiar la contraseña dentro de la app. Incluye un objeto con la info del usuario. 
def changepass(request,id):
    obj = Usuario.objects.get(id=id)
    return render(request,'changepass.html')
# Metodo que recibe los parametros del formulario changepass para actualizar la constraseña a un usuario. Una vez la contraseña haya sido cambiada, termina sesión y 
# manda al index
def updatepass(request,id):
    obj = Usuario.objects.get(id=id)
    obj.set_password(request.GET['password'])
    obj.save()
    json = {
        "info" : Usuario.objects.all()
    }
    return render(request,'index.html',context=json)
# Dirreciona al about
def about(request):
    return render(request,'about.html')
# Direcciona a contacto
def contacto(request):
    return render(request,'contacto.html')
# Direcciona a la informacion detallada de una aplicacion, incluyendo un objeto con cierta informacion que se desplegará en la plantilla.
def detalleapp(request, id):
    obj = App.objects.get(id=id)
    json = {
        "pk": obj.pk,
        "authorApp" : obj.authorApp,
        "title" : obj.title,
        "description" : obj.description,
        "imageApp" : obj.imageApp,
        "date": obj.date
    }
    return render(request,'detalleapp.html',context=json)
# Direcciona a los comentarios hechos sobre una app determinada, incluye un objeto con todos los comentarios que posteriormente se filtran en el html.
def comentarios(request,id):
  app = App.objects.get(id=id)
  cmt = Comment.objects.all()
  json = {
    "id_app": app.pk,
    "cmt": cmt
  }
  return render(request,'comentarios.html', context=json)
# Direcciona al formulario para crear un comentario, incluye el id de la app a la que se le va a escribir el comentario
def createcomentario(request,id):
  json = {
    "id_app": id
  }
  return render(request, 'createcomentario.html', context=json)
# Metodo que crea el comentario sobre una app en la bd, una vez temrinado, lo guarda y direcciona a los comentarios.
def newcomentario(request):
  cmt = Comment()
  obj = Usuario.objects.get(id=request.GET['authorcomment'])
  cmt.authorComment = obj
  app = App.objects.get(id=request.GET['id_app'])
  cmt.id_app = app
  cmt.title = request.GET['title']
  cmt.stars = request.GET['stars']
  cmt.comment = request.GET['comment']
  import datetime
  cmt.date = datetime.datetime.now()
  cmt.save()
  json = {
    'id_app': request.GET['id_app'],
    'cmt': Comment.objects.all()
  }
  return render(request,'comentarios.html', context=json)
# Direcciona al formulario para volverte developer
def developer(request):
  return render(request, 'developer.html')
# Una vez el sistema lo analiza, manda la información hacia este metodo el cual lo guarda en la tabla developer y le cambia el rol al usaurio como developer para que se le 
# puedan mostrar opciones que omco usuario normal no le es posible. Una vez terminado, direcciona a home.
def newdeveloper(request):
  dev = Developer()
  obj = Usuario.objects.get(id=request.GET['id_developer'])
  dev.id_developer = obj
  dev.name = request.GET['name']
  dev.description = request.GET['description']
  import datetime
  dev.date = datetime.datetime.now()
  dev.save()
  obj.rol = 'developer'
  obj.save()
  return render(request, 'home.html')
# Direccion al formulario para registrar una nueva app
def createapp(request):
  form_class = App
  return render(request, 'createapp.html')
# Metodo que obtiene los parametros enviados por el formulario para crear un nuevo objeto dentro de la base de datos. Una vez termina esto, direcciona a home.
def newapp(request):
  app = App()
  dev = Developer.objects.get(id_developer=request.GET['authorApp'])
  app.authorApp = dev
  app.title = request.GET['title']
  app.description = request.GET['description']
  app.imageApp = 'static/img/bd/app/'+request.GET['imageApp']
  import datetime
  app.date = datetime.datetime.now()
  app.save()
  return render(request, 'home.html')
# Metodo que elimina una aplicacion definitivamente de la pagina.
def deleteapp(request,id):
    app = App.objects.get(id=id)
    app.delete()
    return render(request, 'home.html')
# Direcciona al formulario para editar la info de una app, incluye un objeto app.
def editapp(request,id):
    app = App.objects.get(id=id)
    json = {
        'info':app
    }
    return render(request, 'editapp.html', context=json)
# Metodo que actualiza la informacion de una aplicacion con los parametros obtenidos desde el formulario. Una vez hace los cambios y los guarda. Direcciona a home.
def updateapp(request,id):
    obj = App(id=id)
    dev = Developer.objects.get(id_developer=request.GET['authorApp'])
    obj.authorApp = dev
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.imageApp = 'static/img/bd/app/'+request.GET['imageApp']
    import datetime
    obj.date = datetime.datetime.now()
    obj.save()
    json = {
        "info" : App.objects.all()
    }
    return render(request,'home.html',context=json)