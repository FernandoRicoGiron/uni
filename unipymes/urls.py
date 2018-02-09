from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index),
    path('contactanos/', views.contactanos),
    path('evaluacion/', views.evaluacion),
    path('servicios/', views.servicios),
    path('quienessomos/', views.quienessomos),
    path('inisiarsesion/', views.login),
    path('registro/', views.registro),
    path('registrar/', views.registrar),
    path('iniciosesion/', views.iniciarsesion),
    path('cerrarsesion/', views.cerrarsesion),
    re_path('servicios/(?P<id>\d+)/', views.servicio),
    path('solicitado/', views.solicitado),
    path('mensaje/', views.mensaje),
    path('mensaje_encuesta/', views.encuesta),
    path('olvidocontraseña/', views.olvidocontraseña),
    path('nuevacontraseña/', views.nuevacontraseña),
    path('crearnuevacontra/', views.crearnuevacontra),
    re_path('salto/(?P<usuario>[\w.@+-]+)/', views.salto),
    path('modificarcontraseña/', views.modificarcontraseña),
    path('moddatos/', views.modificarperfil),
    path('editperfil/', views.editar_perfil),
    path('estadosoli/', views.estadosoli),
    path('validarusuyemp/', views.validarusuyemp),
]