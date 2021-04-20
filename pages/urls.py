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
    path('comentarios/',views.comentarios,name='comentarios')
]