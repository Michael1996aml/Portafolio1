from pyexpat import model
from re import U
from statistics import mode
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Cliente, Perfil, Abogado

class registrarForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['first_name','last_name','username','email','password1','password2','groups']
        help_texts = {k:""for k in fields}

class perfilForm(forms.ModelForm):
    class Meta:
        model= Perfil
        fields=  ['nombre','apellido','fono','direccion','email','fono','fecha_nac','image']

class agregarcliFrom(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_cliente','apellido_cliente','fono_cliente','direccion_cliente']

class agregaraboFrom(forms.ModelForm):
    class Meta:
        model = Abogado
        fields = ['nombre_abogado','apellido_abogado','fono_abogado','direccion_abogado','email_abogado']
