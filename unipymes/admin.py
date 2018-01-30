from django.contrib import admin
from .models import *

class Usuarios(admin.ModelAdmin):
	list_display = ["id","Usuario"]
	list_display_links = ["Usuario"]
	search_fields = ['Usuario']
	 
	class Meta:
		model = Usuario

class Empresas(admin.ModelAdmin):
	list_display = ["id","DenominacionSocial"]
	list_display_links = ["DenominacionSocial"]
	search_fields = ['DenominacionSocial']
	 
	class Meta:
		model = Empresa

class Escuelas(admin.ModelAdmin):
	list_display = ["id","Nombre"]
	list_display_links = ["Nombre"]
	search_fields = ['Nombre']
	 
	class Meta:
		model = Escuela

class Servicios(admin.ModelAdmin):
	list_display = ["id","Nombre"]
	list_display_links = ["Nombre"]
	search_fields = ['Nombre']
	 
	class Meta:
		model = Servicio

class Carreras(admin.ModelAdmin):
	list_display = ["id","Nombre"]
	list_display_links = ["Nombre"]
	search_fields = ['Nombre']
	 
	class Meta:
		model = Carrera		

class Mensajes(admin.ModelAdmin):
	list_display = ["id","Nombre","Empresa","Estado"]
	list_display_links = ["Nombre"]
	search_fields = ['Nombre']
	 
	class Meta:
		model = Mensaje	

class Solicitudes(admin.ModelAdmin):
	list_display = ["id","get_Serv","get_Usu","get_Empre"]
	list_display_links = ["get_Serv"]
	search_fields = ['get_Serv']

	def get_Usu(self, obj):
		return obj.Usuarios_idUsuario.Usuario

	def get_Serv(self, obj):
		return obj.Servicios_idServicios.Nombre

	def get_Empre(self, obj):
		return obj.Empresas_idEmpresa.DenominacionSocial
	get_Usu.short_description = 'Usuario'
	get_Serv.short_description = 'Servicio'
	get_Empre.short_description = 'Empresa'
	 
	class Meta:
		model = Solicitude	

class Esperas(admin.ModelAdmin):
	list_display = ["id","get_Serv","get_Usu","get_Empre"]
	list_display_links = ["get_Serv"]
	search_fields = ['get_Serv']

	def get_Usu(self, obj):
		return obj.Usuarios_idUsuario.Usuario

	def get_Serv(self, obj):
		return obj.Servicios_idServicios.Nombre

	def get_Empre(self, obj):
		return obj.Empresas_idEmpresa.DenominacionSocial
	get_Usu.short_description = 'Usuario'
	get_Serv.short_description = 'Servicio'
	get_Empre.short_description = 'Empresa'
	 
	class Meta:
		model = Espera
				

admin.site.register(Usuario, Usuarios)
admin.site.register(Empresa, Empresas)
admin.site.register(Encuesta)
admin.site.register(Escuela, Escuelas)
admin.site.register(Solicitude, Solicitudes)
admin.site.register(Servicio, Servicios)
admin.site.register(Mensaje, Mensajes)
admin.site.register(Espera, Esperas)
admin.site.register(Carrera, Carreras)