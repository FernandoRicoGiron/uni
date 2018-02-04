from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.http import JsonResponse

def index(request):
	return render(request, 'index.html', {})

def contactanos(request):
	return render(request, 'contacto.html', {})
def evaluacion(request):
	return render(request,'eval1.html',{})

@csrf_exempt
def servicios(request):
	servicio = Servicio.objects.all()
	escuela = Escuela.objects.all()
	carreras = Carrera.objects.all()
	return render(request, 'servicios.html', {'servicio':servicio, 'escuela':escuela, 'carreras':carreras})

def quienessomos(request):
	return render(request, 'services.html', {})

def login(request):
	if request.method == 'POST':
	#POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
		if request.is_ajax():
			usuario = Usuario.objects.filter(Usuario=request.POST.get("email"),Contraseña=request.POST.get("password")).exists()
			if usuario==True:
				request.session ['sesion'] = request.POST.get("usuario")
				if 'regreso' in request.POST:
					servicio = Servicio.objects.all()
					escuela = Escuela.objects.all()
					return render(request, 'servicios.html', {'servicio':servicio, 'escuela':escuela})
				else:
					return render(request, 'index.html', {})
			else:
				usucon = "mal"
				data = {"usucon":usucon}
				#Returning same data back to browser.It is not possible with Normal submit
				return JsonResponse(data)
   				 #Get goes here
	return render(request, 'login.html')

def registro(request):
	return render(request, 'registro.html', {})

@csrf_exempt
def servicio(request, id):
	servicio = Servicio.objects.get(id=id)
	servicios = Servicio.objects.filter(Carrera=servicio.Carrera)
	print(servicio)
	escuela = Escuela.objects.all()
	return render(request, 'servicio.html', {'servicio':servicio, 'servicios':servicios})

@csrf_exempt
def registrar(request):
	Empresa.objects.create(DenominacionSocial=request.POST.get("densocial"), RFC=request.POST.get("rfc"), Telefono=request.POST.get("telempresa"),
		Calle=request.POST.get("calleempresa"),NumExterior=request.POST.get("numexteemp"), NumInterior=request.POST.get("numinteemp"), CodigoPostal=request.POST.get("codigopostalemp"),
		SitioWeb=request.POST.get("sitio"))

	densocial = Empresa.objects.get(DenominacionSocial=request.POST.get("densocial"))
	Usuario.objects.create(Empresas_idEmpresas=densocial, Nombre=request.POST.get("name"), ApellidoP=request.POST.get("apellidoP"),
		ApellidoM=request.POST.get("apellidoM"),FechaNacimiento=request.POST.get("fecha"), NumTelefono=request.POST.get("telefono"), EstadoCivil=request.POST.get("ecivil"),
		Sexo=request.POST.get("sexo"),Escolaridad=request.POST.get("escolaridad"),Estado=request.POST.get("estado"),Municipio=request.POST.get("municipio"),
		Domicilio=request.POST.get("domicilio"),NumExterior=request.POST.get("numexterior"),NumInterior=request.POST.get("numinterior"),CodigoPostal=request.POST.get("codigopostal"),
		Correo=request.POST.get("correo"),Usuario=request.POST.get("usuario"),Contraseña=request.POST.get("contraseña"))
	return render(request, 'login.html', {})

def iniciarsesion(request):
	usuario = Usuario.objects.filter(Usuario=request.POST.get("usuario"),Contraseña=request.POST.get("password")).exists()
	if usuario==True:
		request.session ['sesion'] = request.POST.get("usuario")
		if 'regreso' in request.POST:
			servicio = Servicio.objects.all()
			escuela = Escuela.objects.all()
			return render(request, 'servicios.html', {'servicio':servicio, 'escuela':escuela})
		else:
			return render(request, 'index.html', {})
	else:
		usucon = "El usuario o la contraseña es incorrecto"
		return render(request, 'login.html', {'usucon':usucon})

def cerrarsesion(request):
	request.session.flush()
	return render(request, 'index.html', {})

@csrf_exempt
def solicitado(request):
	if 'sesion' in request.session:
		usuario = Usuario.objects.get(Usuario=request.POST.get('sesion'))
		empresa = Empresa.objects.get(DenominacionSocial=usuario.Empresas_idEmpresas)
		servicio = Servicio.objects.get(Nombre=request.POST.get('nombreser'))
		if 'espera' in request.POST:
			Espera.objects.create(Usuarios_idUsuario=usuario, Empresas_idEmpresa = empresa,Servicios_idServicios=servicio)
		else:
			Solicitude.objects.create(Usuarios_idUsuario=usuario, Empresas_idEmpresa = empresa,Servicios_idServicios=servicio, Estado="0")
		email = EmailMessage('Solicitud de Servicio', 'El usuario '+ request.POST.get('sesion') +' a solicitado un ' + request.POST.get('nombreser'), to = ['riicoo28@gmail.com'])
		email.send()
		return render(request, 'solicitado.html', {})
	else:
		sesion = "Debe iniciar sesion para continuar"
		return render(request, 'login.html', {'sesion':sesion})

@csrf_exempt
def mensaje(request):
	Mensaje.objects.create(Nombre=request.POST.get("nombre"), Correo=request.POST.get("correo"), Empresa=request.POST.get("empresa"),
		Asunto=request.POST.get("asunto"),Texto=request.POST.get("mensaje"))

	email = EmailMessage('Contacto', 'La persona '+ request.POST.get("nombre") +' de la empresa ' + request.POST.get("empresa") + ' con el correo '+request.POST.get("correo")+" desea saber la siguiente informacion:\n"+request.POST.get("asunto") +'\n' +request.POST.get("mensaje"),to = ['riicoo28@gmail.com'])
	email.send()
	return render(request, 'mensaje.html', {})

@csrf_exempt
def encuesta(request):
	usu = Usuario.objects.get(Usuario=request.session['sesion'])
	Encuesta.objects.create(Empresas_idEmpresa=usu.Empresas_idEmpresas,
		Uno=request.POST.get("uno"),
		Dos=request.POST.get("dos"),
		Tres=request.POST.get("tres"),
		Cuatro=request.POST.get("cuatro"),
		Cinco=request.POST.get("cinco"))
	return render(request, 'mensaje_encuesta.html', {})	

def nuevacontraseña(request):
	correo = Usuario.objects.filter(Correo=request.POST.get("email")).exists()
	if correo==True:
		usuario = Usuario.objects.get(Correo=request.POST.get("email"))
		sesion = "Se ha enviado un enlace a su correo para que recupere su contraseña"
		email = EmailMessage('Recuperar contraseña de Unipymes', 'Para poder ingresar de nuevo a unipymes de click en el siguiente enlace\nhttp://www.unipymes.com.mx/salto/'+usuario.Usuario+"/",to = [request.POST.get("email")])
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
	usuario = Usuario.objects.get(Usuario=request.POST.get('usuario'))
	usuario.Contraseña = request.POST.get("nuevacontraseña")
	usuario.save()
	return render(request, 'login.html', {'usuario':usuario})

def modificarperfil(request):
	usuario = Usuario.objects.get(Usuario=request.session['sesion'])
	return render(request, 'moddatos.html', {'usuario':usuario})

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

	usuario = Usuario.objects.get(Usuario=request.session["sesion"])
	usuario.Empresas_idEmpresas=empresa
	usuario.Nombre=request.POST.get("name")
	usuario.ApellidoP=request.POST.get("apellidoP")
	usuario.ApellidoM=request.POST.get("apellidoM")
	usuario.FechaNacimiento=request.POST.get("fecha")
	usuario.NumTelefono=request.POST.get("telefono")
	usuario.EstadoCivil=request.POST.get("ecivil")
	usuario.Sexo=request.POST.get("sexo")
	usuario.Escolaridad=request.POST.get("escolaridad")
	usuario.Estado=request.POST.get("estado")
	usuario.Municipio=request.POST.get("municipio")
	usuario.Domicilio=request.POST.get("domicilio")
	usuario.NumExterior=request.POST.get("numexterior")
	usuario.NumInterior=request.POST.get("numinterior")
	usuario.CodigoPostal=request.POST.get("codigopostal")
	usuario.Correo=request.POST.get("correo")
	usuario.Usuario=request.POST.get("usuario")
	usuario.Contraseña=request.POST.get("contraseña")
	usuario.save()

	return render(request, 'index.html', {})

def estadosoli(request):
	solicitudes = Solicitude.objects.filter(Usuarios_idUsuario__Usuario=request.session["sesion"])
	return render(request, 'estadosoli.html', {"solicitudes":solicitudes})