from django.views.generic import TemplateView
from django.shortcuts import render
from users.models import *
from django.http import HttpResponse,JsonResponse

def index(request):
    return render(request,'index.html')

def home(request):
    json = {
        "info" : App.objects.all()
    }
    return render(request,'home.html',context=json)

def user(request):
    json = {
        "info" : Usuario.objects.all()
    }
    return render(request,'user.html')

def editUser(request,id):
    obj = Usuario.objects.get(id=id)
    json = {
        "edad" : obj.edad,
        "Telefono" : obj.telefono,
    }
    return render(request,'edituser.html',context=json)

def updateuser(request,id):
    obj = Usuario.objects.get(id=id)
    obj.edad = request.GET['edad']
    obj.telefono = request.GET['Telefono']
    obj.save()
    json = {
        "info" : Usuario.objects.all()
    }
    return render(request,'user.html',context=json)

def changepass(request,id):
    obj = Usuario.objects.get(id=id)
    return render(request,'changepass.html')

def updatepass(request,id):
    obj = Usuario.objects.get(id=id)
    obj.set_password(request.GET['password'])
    obj.save()
    json = {
        "info" : Usuario.objects.all()
    }
    return render(request,'user.html',context=json)

def about(request):
    return render(request,'about.html')

def contacto(request):
    return render(request,'contacto.html')

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

def editApp(request,id):
    obj = App.objects.get(id=id)
    json = {
        "authorApp" : obj.authorApp,
        "title" : obj.title,
        "description" : obj.description,
        "imageApp" : obj.imageApp
    }
    return render(request,'edit.html',context=json)

def updateApp(request,id):
    obj = App(id=id)
    obj.authorApp = request.GET['authorApp']
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.imageApp = request.GET['imageApp']
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at
    obj.save()
    json = {
        "info" : App.objects.all()
    }
    return render(request,'home.html',context=json)

def comentarios(request,id):
  app = App.objects.get(id=id)
  cmt = Comment.objects.all()
  json = {
    "id_app": app.pk,
    "cmt": cmt
  }
  return render(request,'comentarios.html', context=json)

def createcomentario(request,id):
  json = {
    "id_app": id
  }
  return render(request, 'createcomentario.html', context=json)

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

def developer(request):
  return render(request, 'developer.html')

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