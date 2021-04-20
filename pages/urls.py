from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.index,name='index'),
    path('home/', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('contacto/',views.contacto,name='contacto'),
    path('user/',views.user,name='user'),
    path('edituser/<int:id>',views.editUser,name='edituser'),
    path('updateuser/<int:id>',views.updateuser,name='updateuser'),
    path('changepass/<int:id>',views.changepass,name='changepass'),
    path('updatepass/<int:id>',views.updatepass,name='updatepass'),
    path('detalleapp/<int:id>',views.detalleapp,name='detalleapp'),
    path('comentarios/<int:id>',views.comentarios,name='comentarios'),
    path('createcomentario/<int:id>',views.createcomentario,name='createcomentario'),
    path('newcomentario/',views.newcomentario,name='newcomentario'),
    path('developer/',views.developer,name='developer'),
    path('newdeveloper/',views.newdeveloper,name='newdeveloper'),
    path('createapp/',views.createapp,name='createapp'),
    path('newapp/',views.newapp,name='newapp'),
    
]