from django.shortcuts import render, render_to_response, redirect, reverse
from django.utils import timezone
from .models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.mail import EmailMessage
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import *
import json
import smtplib
import sweetify
from django import template
register = template.Library()

def min_length(a, b):
	if len(a) < b:
		raise ValueError("Asegurece de que ingresa los datos correctamente")
	else:
		return True

def index(request):
	reseñas = Reseña.objects.all()
	return render(request, 'index.html', {"resenas":reseñas})

def google(request):
	return render(request, 'googleb8e411affc4ac215.html', {})

def contactanos(request):
	return render(request, 'contacto.html', {})
def evaluacion(request):
	return render(request,'eval1.html',{})

@csrf_exempt
def servicios(request):
	servicio = Servicio.objects.all()
	sumaserv=0
	for serv in servicio:
		sumaserv+=1
	areas = Area.objects.all()
	return render(request, 'servicios.html', {'servicio':servicio, 'areas':areas, "numserv":sumaserv})

def quienessomos(request):
	return render(request, 'services.html', {})

def iniciarsesion(request):
	usuario = request.POST.get("usuario")
	password = request.POST.get("password")
	try:
		usuario = authenticate(request, username=usuario, password=password)
		login(request, usuario)
		return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
	except Exception as e:
		sweetify.error(request, 'Oops!', text='El usuario o la contraseña es incorrecto', persistent=':´(')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

@csrf_exempt
def modpassword(request):
	usuario = request.user
	if usuario.check_password(request.POST.get("oldpassword")):
		if request.POST.get("newpassword") == request.POST.get("confirmpassword"):
			usuario.set_password(request.POST.get("newpassword"))
			usuario.save()
			login(request, usuario)
			sweetify.success(request, 'Genial!', text='La contraseña a sido modificada correctamente', persistent=':)')
			return HttpResponseRedirect("/")
		else:
			sweetify.error(request, 'Oops!', text='Las contraseñas no coinciden', persistent=':´(')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
	else:
		sweetify.error(request, 'Oops!', text='La contraseña antigua no coincide', persistent=':´(')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
	

def logint(request):
	return render(request, 'login.html')

def registro(request):
	return render(request, 'registro.html', {})

@csrf_exempt
def servicio(request, id):
	servicio = Servicio.objects.get(id=id)
	servicios = Servicio.objects.filter(Area=servicio.Area)
	return render(request, 'servicio.html', {'servicio':servicio, 'servicios':servicios})

@csrf_exempt
def registrar(request):
	usuario = request.POST.get("usuario")
	email = request.POST.get("correo")
	password = request.POST.get("contraseña")
	nombre = request.POST.get("nombre")
	apellido = request.POST.get("apellido")
	densocial = request.POST.get("densocial")
	user = User.objects.filter(username=usuario).exists()
	nomempresa = Empresa.objects.filter(DenominacionSocial=densocial).exists()
	if user == False:
		if nomempresa == False:
			user = User.objects.create_user(username=usuario,
				email=email,
				password=password,
				first_name=nombre,
				last_name=apellido)
			user = authenticate(request, username=usuario, password=password)
			login(request, user)
			Empresa.objects.create(Usuario = user, DenominacionSocial=densocial)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
		else:
			sweetify.error(request, 'Oops!', text='La empresa ya existe', persistent=':´(')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
	else:
		sweetify.error(request, 'Oops!', text='El usuario ya existe', persistent=':´(')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def validarusuyemp(request):
	data={}
	usuario = Usuario.objects.filter(Usuario=request.POST.get("usuario")).exists()
	empresa = Empresa.objects.filter(DenominacionSocial=request.POST.get("empresa")).exists()
	if usuario==False:
		data["usu"]="bien"
	else:
		data["usu"]="mal"
	if empresa==False:
		data["denso"]="bien"
	else:
		data["denso"]="mal"
	return JsonResponse(data)

def cerrarsesion(request):
	logout(request)
	return HttpResponseRedirect("/")

@csrf_exempt
def solicitado(request):
	if request.user.is_authenticated:
		usuario = request.user
		empresa = Empresa.objects.get(Usuario = usuario)
		servicio = Servicio.objects.get(Nombre=request.POST.get('nombreser'))
		if 'espera' in request.POST:
			Espera.objects.create(Usuario=usuario, Empresa = empresa, Servicio=servicio)
		else:
			Solicitude.objects.create(Usuario=usuario, Empresa = empresa,Servicio=servicio, Estado="0")
		email = EmailMessage('Solicitud de Servicio', 'El usuario '+ usuario.username +' a solicitado un ' + request.POST.get('nombreser'), to = ['contacto@unipymes.com.mx'])
		email.send()
		return render(request, 'solicitado.html', {})
	else:
		sesion = "Debe iniciar sesion para continuar"
		return render(request, 'login.html', {'sesion':sesion})

@csrf_exempt
def mensaje(request):
	try:
		validate_email(request.POST.get("correo"))
		min_length(request.POST.get("nombre"),3)
		min_length(request.POST.get("empresa"),3)
		min_length(request.POST.get("asunto"),3)
		min_length(request.POST.get("mensaje"),5)
		Mensaje.objects.create(Nombre=request.POST.get("nombre"),
			Correo=request.POST.get("correo"),
			Empresa=request.POST.get("empresa"),
			Asunto=request.POST.get("asunto"),
			Texto=request.POST.get("mensaje"))

		email = EmailMessage('Contacto', 'La persona '+ request.POST.get("nombre") +' de la empresa ' + request.POST.get("empresa") + ' con el correo '+request.POST.get("correo")+" desea saber la siguiente informacion:\n"+request.POST.get("asunto") +'\n' +request.POST.get("mensaje"),to = ['contacto@unipymes.com.mx'])
		email.send()
		return render(request, 'mensaje.html', {})
	except Exception as e:
		sweetify.error(request, 'Oops!', text=str(e).replace("['","").replace("']",""), persistent=':´(')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
	

@csrf_exempt
def encuesta(request):
	empresa = Empresa.objects.get(Usuario=request.user)
	Encuesta.objects.create(Empresa=empresa,
		Consideracion=request.POST.get("uno"),
		Mejoras=request.POST.get("dos"),
		Calificacion_Producto=request.POST.get("tres"),
		Para_Mejorar=request.POST.get("cuatro"),
		Recomendacion=request.POST.get("cinco"),
		Comentarios=request.POST.get("comentarios"))
	return render(request, 'mensaje_encuesta.html', {})

def nuevacontraseña(request):
	correo = Dato.objects.filter(Correo=request.POST.get("email")).exists()
	if correo==True:
		usuario = Dato.objects.get(Correo=request.POST.get("email"))
		sesion = "Se ha enviado un enlace a su correo para que recupere su contraseña"
		email = EmailMessage('Recuperar contraseña de Unipymes', 'Para poder ingresar de nuevo a unipymes de click en el siguiente enlace\nhttp://www.unipymes.com.mx/salto/'+usuario.Usuario.username+"/",to = [request.POST.get("email")])
		email.send()
		return render(request, 'olvidocontra.html', {'sesion':sesion,})
	else:
		sesion = "El correo que a ingresado no tiene una cuenta"
		return render(request, 'olvidocontra.html', {'sesion':sesion})

@csrf_exempt
def olvidocontraseña(request):
	return render(request, 'olvidocontra.html', {})

def salto(request, usuario):
	return render(request, 'salto.html', {'usuario':usuario})

def crearnuevacontra(request):
	usuario = request.POST.get("usuario")
	return render(request, 'nuevacontraseña.html', {'usuario':usuario})


def modificarcontraseña(request):
	usuario = Dato.objects.get(Usuario=request.POST.get('usuario'))
	usuario.Contraseña = request.POST.get("nuevacontraseña")
	usuario.save()
	return render(request, 'login.html', {'usuario':usuario})

def modificarperfil(request):
	usuario = Dato.objects.get(Usuario=request.user)
	empresa = Empresa.objects.get(Usuario=request.user)
	return render(request, 'moddatos.html', {'usuario':usuario, 'empresa':empresa})

@csrf_exempt
def editar_perfil(request):
	empresa = Empresa.objects.get(DenominacionSocial=request.POST.get("densocial"))
	empresa.DenominacionSocial=request.POST.get("densocial")
	empresa.RFC=request.POST.get("rfc")
	empresa.Telefono=request.POST.get("telempresa")
	empresa.Calle=request.POST.get("calleempresa")
	empresa.NumExterior=request.POST.get("numexteemp")
	empresa.NumInterior=request.POST.get("numinteemp")
	empresa.CodigoPostal=request.POST.get("codigopostalemp")
	empresa.SitioWeb=request.POST.get("sitio")
	empresa.save()
	usuario = request.user
	usuario.first_name=request.POST.get("name")
	usuario.last_name=request.POST.get("apellido")

	datos = Dato.objects.get(Usuario = usuario)

	datos.FechaNacimiento=request.POST.get("fecha")
	datos.Telefono=request.POST.get("telefono")
	datos.EstadoCivil=request.POST.get("ecivil")
	datos.Sexo=request.POST.get("sexo")
	datos.Escolaridad=request.POST.get("escolaridad")
	datos.Estado=request.POST.get("estado")
	datos.Municipio=request.POST.get("municipio")
	datos.Domicilio=request.POST.get("domicilio")
	datos.NumExterior=request.POST.get("numexterior")
	datos.NumInterior=request.POST.get("numinterior")
	datos.CodigoPostal=request.POST.get("codigopostal")
	usuario.save()
	datos.save()
	reseñas = Reseña.objects.all()
	sweetify.success(request, 'Genial!', text='Sus datos han sido modificados correctamente', persistent=':)')
	return render(request, 'index.html', {"resenas":reseñas})

@login_required(login_url='/')
def estadosoli(request):
	solicitudes = Solicitude.objects.filter(Usuario=request.user)
	dato = Dato.objects.get(Usuario=request.user)
	if dato.Encargado == True:
		solicitudes = Solicitude.objects.filter(Encargado = request.user)
		return render(request, "encargados.html", {"solicitudes":solicitudes})
	else:
		return render(request, 'estadosoli.html', {"solicitudes":solicitudes})

@csrf_exempt
def MensajeSoli(request):
	print(request.FILES)
	if request.FILES:
		mensaje = Mensaje_Solicitud.objects.create(
			Mensaje = request.POST.get("mensaje"),
			Usuario = request.user,
			Archivo = request.FILES["file"])
	else:
		mensaje = Mensaje_Solicitud.objects.create(
			Mensaje = request.POST.get("mensaje"),
			Usuario = request.user,)
	solicitud = Solicitude.objects.get(id=request.POST.get("solicitud"))
	solicitud.Mensaje_Solicitud.add(mensaje)
	if request.user == solicitud.Encargado:
		email = EmailMessage('Mensaje de Unipymes', 'Tienes un mensaje en el sitio de unipymes para verificarlo visita\nwww.unipymes.com.mx',to = [request.user.email])
	else:
		email = EmailMessage('Mensaje de Unipymes', 'El cliente '+request.user.username+' te ha enviado un mensaje en\nwww.unipymes.com.mx',to = [solicitud.Encargado.email])
	email.send()
	sweetify.success(request, 'Genial!', text="Su mensaje a sido enviado correctamente", persistent=':)')
	return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

@csrf_exempt
def solicitud_es(request):
	data = {}
	solicitud = Solicitude.objects.get(id = request.POST.get("id"))
	data = {"id":solicitud.id, "servicio":solicitud.Servicio.Nombre, "mensajes":{}}
	for x in solicitud.Mensaje_Solicitud.all():
		if x.Archivo:
			data["mensajes"][x.id] = {"mensaje":x.Mensaje,
			"url":x.Archivo.url,
			"nombrearchivo":x.Archivo.name,
			"date":x.date.strftime("%Y-%m-%d %H:%M"),
			"usuario":x.Usuario.username}	
		else:
			data["mensajes"][x.id] = {"mensaje":x.Mensaje,
			"url":"",
			"nombrearchivo":"",
			"date":x.date.strftime("%Y-%m-%d %H:%M"),
			"usuario":x.Usuario.username}	
	
	return JsonResponse(data)


############# BLOG ####################
def blog(request):
	obtener_posts = Post.objects.all()
	posts = obtener_posts[::-1]

	return render(request, "blog.html",{"posts":posts})


def blog_detalle(request,id):
	post = Post.objects.get(id=id)
	mis_post = Post.objects.all()
	posts = mis_post[::-1]

	return render(request, "blog_detalle.html", {"post":post,"posts":posts})
	
