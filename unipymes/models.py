from __future__ import unicode_literals
import os, sys
from django.db import models
from django.utils import timezone
import datetime
from django.db import migrations
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
import json
from django.utils import timezone

ESTADO_SOLICITUDES = (
	('0','Solicitud Enviada'),
	('10','Solicitud Recibida'),
	("20",'Se Realizó la Primera Reunión'),
	("40",'Se Realizó la primer Revisión'),
	("60",'Se Realizó la segunda Revisión'),
	("80",'Se Realizó la tercera Revisión'),
	("90",'Se Realizó la Entrega'),
	("100",'Finalizado'),
)

ESTADO_MENSAJES = (
	('Sin Responder','Sin Responder'),
	('Respondido','Respondido'),
)

class Dato(models.Model):
	Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	FechaNacimiento = models.DateField(blank=True, null=True)
	Telefono = models.CharField(max_length=50, blank=True, null=True)
	EstadoCivil = models.CharField(max_length=50, blank=True, null=True)
	Sexo = models.CharField(max_length=50, blank=True, null=True)
	Escolaridad = models.CharField(max_length=50, blank=True, null=True)
	Estado = models.CharField(max_length=50, blank=True, null=True)
	Municipio = models.CharField(max_length=50, blank=True, null=True)
	Domicilio = models.CharField(max_length=50, blank=True, null=True)
	NumExterior = models.CharField(max_length=50, blank=True, null=True)
	NumInterior = models.CharField(max_length=50, blank=True, null=True)
	CodigoPostal = models.CharField(max_length=50, blank=True, null=True)
	Correo = models.EmailField(blank=True, null=True)
	Encargado = models.BooleanField(default=False)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Dato.objects.create(Usuario=instance)

	def __str__(self):
		return self.Usuario.username

class Empresa(models.Model):
	Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	DenominacionSocial = models.CharField(max_length=50, blank=False, unique=True)
	RFC = models.CharField(max_length=50, blank=True, null=True)
	Telefono = models.CharField(max_length=50, blank=True, null=True)
	Calle = models.CharField(max_length=50, blank=True, null=True)
	NumExterior = models.CharField(max_length=50, blank=True, null=True)
	NumInterior = models.CharField(max_length=50, blank=True, null=True)
	CodigoPostal = models.CharField(max_length=50, blank=True, null=True)
	SitioWeb = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.DenominacionSocial

class Area(models.Model):
	Area = models.CharField(max_length=100)

	def __str__(self):
		return self.Area

class Servicio(models.Model):
	Nombre = models.CharField(max_length=100)
	Descripcion = models.TextField()
	Disponible = models.IntegerField(default=0)
	Imagen = models.ImageField(upload_to = 'Servicios')
	Precio = models.CharField(max_length=50)
	Area = models.ForeignKey('Area', on_delete=models.CASCADE)

	def __str__(self):
		return self.Nombre

class Mensaje_Solicitud(models.Model):
	Mensaje = models.TextField()
	Archivo = models.FileField(upload_to = 'Mensajes', blank=True, null=True)
	Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now)

	def filename(self):
		return os.path.basename(self.Archivo.name)

	def __str__(self):
		return self.Usuario.username

class Solicitude(models.Model):
	Usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cliente')
	Encargado = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='encargado')
	Empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
	Servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
	Estado = models.CharField(max_length=50, choices=ESTADO_SOLICITUDES)
	Mensaje_Solicitud = models.ManyToManyField(Mensaje_Solicitud, blank=True)

	def __str__(self):
		return self.Servicio.Nombre



class Mensaje(models.Model):
	Nombre = models.CharField(max_length=50)
	Correo = models.CharField(max_length=50)
	Empresa = models.CharField(max_length=50)
	Asunto = models.CharField(max_length=50)
	Texto = models.TextField()
	Estado = models.CharField(max_length=50, default="Sin Responder", choices=ESTADO_MENSAJES)

	def __str__(self):
		return self.Asunto

class Espera(models.Model):
	Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	Empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
	Servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)

	def __str__(self):
		return self.Servicio.Nombre

class Encuesta(models.Model):
	Empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
	Consideracion = models.CharField(max_length=50)
	Mejoras = models.CharField(max_length=50)
	Calificacion_Producto = models.CharField(max_length=50)
	Para_Mejorar = models.CharField(max_length=50)
	Recomendacion = models.CharField(max_length=50)
	Comentarios = models.TextField()

	def __str__(self):
		return self.Empresa.DenominacionSocial
