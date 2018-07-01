from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, AbstractUser

class Empresas(admin.ModelAdmin):
	list_display = ["id","DenominacionSocial"]
	list_display_links = ["DenominacionSocial"]
	search_fields = ['DenominacionSocial']
	 
	class Meta:
		model = Empresa

class Servicios(admin.ModelAdmin):
	list_display = ["id","Nombre"]
	list_display_links = ["Nombre"]
	search_fields = ['Nombre']
	 
	class Meta:
		model = Servicio		

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
		return obj.Usuario.username

	def get_Serv(self, obj):
		return obj.Servicio.Nombre

	def get_Empre(self, obj):
		return obj.Empresa.DenominacionSocial
		
	get_Usu.short_description = 'username'
	get_Serv.short_description = 'Servicio'
	get_Empre.short_description = 'Empresa'
	 
	class Meta:
		model = Solicitude	

class Esperas(admin.ModelAdmin):
	list_display = ["id","get_Serv","get_Usu","get_Empre"]
	list_display_links = ["get_Serv"]
	search_fields = ['get_Serv']

	def get_Usu(self, obj):
		return obj.Usuario.username

	def get_Serv(self, obj):
		return obj.Servicio.Nombre

	def get_Empre(self, obj):
		return obj.Empresa.DenominacionSocial

	get_Usu.short_description = 'username'
	get_Serv.short_description = 'Servicio'
	get_Empre.short_description = 'Empresa'
	 
	class Meta:
		model = Espera
			

admin.site.register(Dato)
admin.site.register(Empresa, Empresas)
admin.site.register(Encuesta)
admin.site.register(Solicitude, Solicitudes)
admin.site.register(Area)
admin.site.register(Servicio, Servicios)
admin.site.register(Mensaje, Mensajes)
admin.site.register(Espera, Esperas)
admin.site.register(Mensaje_Solicitud)
