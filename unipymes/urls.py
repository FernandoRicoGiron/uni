from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index),
    path('MensajeSoli/', views.MensajeSoli),
    path('solicitud_es/', views.solicitud_es),
    path('contactanos/', views.contactanos),
    path('modpassword/', views.modpassword),
    path('evaluacion/', views.evaluacion),
    path('servicios/', views.servicios),
    path('quienessomos/', views.quienessomos),
    path('blog/', views.blog),
    re_path('blog/(?P<id>\d+)', views.blog_detalle),
    path('inisiarsesion/', views.logint),
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
    path('googleb8e411affc4ac215.html', views.google)
]