from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('contactanos/', views.contactanos),
    path('evaluacion/', views.evaluacion),
    path('servicios/', views.servicios),
    path('quienessomos/', views.quienessomos),
    path('login/', views.login),
    path('registro/', views.registro),
    path('registrar/', views.registrar),
    path('iniciosesion/', views.iniciarsesion),
    path('cerrarsesion/', views.cerrarsesion),
    path('servicio/', views.servicio),
    path('solicitado/', views.solicitado),
    path('mensaje/', views.mensaje),
    path('olvidocontraseña/', views.olvidocontraseña),
    path('nuevacontraseña/', views.nuevacontraseña),
    path('crearnuevacontra/', views.crearnuevacontra),
    path('salto/', views.salto),
    path('modificarcontraseña/', views.modificarcontraseña),
]