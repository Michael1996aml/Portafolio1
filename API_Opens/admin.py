from django.contrib import admin
from .models import Email,Plantilla,Abogado,Solicitud,Documento,Cliente,Bitacora_solicitud,Bitacora_usuario,Perfil

# Register your models here.

admin.site.register(Perfil)
admin.site.register(Email)
admin.site.register(Plantilla)
admin.site.register(Abogado)
admin.site.register(Solicitud)
admin.site.register(Documento)
admin.site.register(Cliente)
admin.site.register(Bitacora_solicitud)
admin.site.register(Bitacora_usuario)

