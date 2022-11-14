from rest_framework import serializers
from django.contrib.auth.models import User,Group
from .models import *

class PlantillaSerializers(serializers.ModelSerializer):
	class Meta:
		model = Plantilla
		fields = '__all__'

class SolicitudSerializers(serializers.ModelSerializer):
        class Meta:
                model = Solicitud
                fields = '__all__'

class DocumentoSerializers(serializers.ModelSerializer):
        class Meta:
                model = Documento
                fields = '__all__'

class ClienteSerializers(serializers.ModelSerializer):
        class Meta:
                model = Cliente
                fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = '__all__'

class GroupSerializers(serializers.ModelSerializer):
        class Meta:
                model = Group
                fields = '__all__'

class AbogadoSerializers(serializers.ModelSerializer):
        class Meta:
                model = Abogado
                fields = '__all__'

