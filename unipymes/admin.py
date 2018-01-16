from django.contrib import admin
from .models import *

class Escuela_has_Servicio(admin.ModelAdmin):
     model= Servicio
     filter_horizontal = ('Escuela',) #If you don't specify this, you will get a multiple select widget.

admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Escuela)
admin.site.register(Solicitude)
admin.site.register(Servicio,Escuela_has_Servicio)
admin.site.register(Mensaje)
admin.site.register(Espera)