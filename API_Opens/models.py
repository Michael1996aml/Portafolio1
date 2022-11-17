from re import A
from statistics import mode
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.



class Perfil(models.Model):
	user= models.OneToOneField(User, on_delete= models.CASCADE)
	nombre = models.CharField(max_length = 200, null=True)
	apellido = models.CharField(max_length = 200, null=True)
	direccion = models.CharField(max_length = 200, null=True)
	email = models.CharField(max_length = 200, null=True)
	fono = models.CharField(max_length = 20, null=True)
	fecha_nac = models.DateField(null=True)
	image= models.ImageField(default='foto.png')
	def __str__(self):
		return f'Perfil de {self.user.username}'



class Email(models.Model):
	nombre = models.CharField(max_length = 200)
	fecha = models.CharField(max_length = 200)
	asunto = models.TextField()
	cuerpo = models.TextField()

	class Meta:
		db_table = 'Email'

	def __str__(self):
		return self.nombre

class Plantilla(models.Model):
	asunto_plantilla = models.TextField()
	cuerpo_plantilla = models.TextField()

	class Meta:
		db_table = 'Plantilla'

	def __str__(self):
		return self.asunto_plantilla

class Cliente(models.Model):
	nombre_cliente = models.CharField(max_length = 200)
	apellido_cliente = models.CharField(max_length = 200)
	fono_cliente = models.CharField(max_length = 200)
	direccion_cliente = models.CharField(max_length = 200)
	user= models.OneToOneField(User, on_delete= models.CASCADE)

	class Meta:
		db_table = 'Cliente'

	def __str__(self):
		return f'Cliente de {self.user.username}'

def createCliente(sender,instance, created, **kwargs,):
		if created:
			Cliente.objects.create(user=instance)
			Abogado.objects.create(user=instance)
post_save.connect(createCliente, sender=User)

class Bitacora_usuario(models.Model):
	fecha = models.DateField()
	hora = models.DateTimeField()
	detalle_bitacora = models.CharField(max_length = 200)

	class Meta:
		db_table = 'Bitacora_usuario'

	def __str__(self):
		return self.fecha

class Abogado(models.Model):
	nombre_abogado = models.CharField(max_length = 200)
	apellido_abogado = models.CharField(max_length = 200)
	fono_abogado = models.CharField(max_length = 200)
	direccion_abogado = models.CharField(max_length = 200)
	email_abogado = models.CharField(max_length = 200)
	user = models.OneToOneField(User, on_delete= models.CASCADE)

	class Meta:
		db_table = 'Abogado'

	def __str__(self):
		return f'Abogado de {self.user.username}'


class Solicitud(models.Model):
	descripcion= models.CharField(max_length = 200)
	fecha =  models.DateTimeField()
	prediccion = models.CharField(max_length = 200)
	id_email = models.ForeignKey('Email' , on_delete = models.SET_NULL, null = True)
	id_abogado = models.ForeignKey('Abogado' , on_delete = models.SET_NULL, null = True)

	class Meta:
		db_table = 'Solicitud'

	def __str__(self):
		return self.descripcion

class Documento(models.Model):
	titulo = models.CharField(max_length = 200)
	documento = models.FileField(upload_to = "Uploaded Files/")
	fecha_documento = models.DateTimeField(auto_now = True)
	user= models.ForeignKey(User, on_delete=models.CASCADE)
	# fecha_documento = models.DateField()
	# solicitud = models.ForeignKey('Solicitud' , on_delete = models.SET_NULL, null = True)

	class Meta:
		db_table = 'Documento'

	

class Bitacora_solicitud(models.Model):
	fecha_solicitud = models.DateField()
	hora_solicitud = models.DateTimeField()
	detalle_solicitud = models.CharField(max_length = 200)
	estado_solicitud = models.CharField(max_length = 200)
	id_solicitud = models.ForeignKey('Solicitud' , on_delete = models.SET_NULL, null = True)

	class Meta:
		db_table = 'Bitacora_solicitud'

	def __str__(self):
		return self.estado_solicitud
