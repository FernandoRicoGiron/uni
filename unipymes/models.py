from django.db import models
from django.utils import timezone

class Empresa(models.Model):
    DenominacionSocial = models.CharField(max_length=50, blank=False, unique=True)
    RFC = models.CharField(max_length=30)
    Telefono = models.CharField(max_length=30)
    Calle = models.CharField(max_length=50)
    NumExterior = models.CharField(max_length=30)
    NumInterior = models.CharField(max_length=30)
    CodigoPostal = models.CharField(max_length=30)
    SitioWeb = models.CharField(max_length=30)

    def __str__(self):
        return self.DenominacionSocial

class Usuario(models.Model):
    Empresas_idEmpresas = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=30)
    ApellidoP = models.CharField(max_length=30)
    ApellidoM = models.CharField(max_length=30)
    FechaNacimiento = models.DateField()
    NumTelefono = models.CharField(max_length=30)
    EstadoCivil = models.CharField(max_length=30)
    Sexo = models.CharField(max_length=30)
    Escolaridad = models.CharField(max_length=30)
    Estado = models.CharField(max_length=30)
    Municipio = models.CharField(max_length=30)
    Domicilio = models.CharField(max_length=30)
    NumExterior = models.CharField(max_length=30)
    NumInterior = models.CharField(max_length=30)
    CodigoPostal = models.CharField(max_length=30)
    Correo = models.CharField(max_length=30)
    Usuario = models.CharField(max_length=30, blank=False, unique=True)
    Contraseña = models.CharField(max_length=30)

    def __str__(self):
        return self.Usuario


class Escuela(models.Model):
    Nombre = models.CharField(max_length=50)
    Estado = models.CharField(max_length=30)
    Municipio = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Servicio(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Disponible = models.IntegerField(default=0)
    Convocatoria = models.ImageField(upload_to = 'Convocatorias')
    Precio = models.CharField(max_length=30)
    Carrera = models.ForeignKey('Carrera', on_delete=models.CASCADE)
    Escuela = models.ForeignKey('Escuela', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id) + " " + self.Nombre

class Carrera(models.Model):
    Nombre = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + " " + self.Nombre


class Solicitude(models.Model):
	Usuarios_idUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
	Empresas_idEmpresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
	Servicios_idServicios = models.ForeignKey('Servicio', on_delete=models.CASCADE)
	Estado = models.CharField(max_length=30)

	def __str__(self):
		return "Solicitud = " + str(self.id) + " Usuario = " + str(self.Usuarios_idUsuario) + " Empresa = " + str(self.Empresas_idEmpresa) + " Estado = " + self.Estado

class Mensaje(models.Model):
    Nombre = models.CharField(max_length=30)
    Correo = models.CharField(max_length=50)
    Empresa = models.CharField(max_length=50)
    Asunto = models.CharField(max_length=30)
    Texto = models.TextField()
    Estado = models.CharField(max_length=30, default="Sin Responder")

    def __str__(self):
        return self.Asunto + " " + self.Estado

class Espera(models.Model):
    Usuarios_idUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    Empresas_idEmpresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    Servicios_idServicios = models.ForeignKey('Servicio', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Servicios_idServicios) + " " + str(self.Usuarios_idUsuario) + " " + str(self.Empresas_idEmpresa)