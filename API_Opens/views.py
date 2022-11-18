import re
from locale import currency
from re import A

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Group, User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import serializers, views, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import permission_required

from .forms import agregarcliFrom, registrarForm, agregaraboFrom
from .models import *
from .serializers import *

# Create your views here.


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers


class PlantillaViewSet(viewsets.ModelViewSet):
    queryset = Plantilla.objects.all()
    serializer_class = PlantillaSerializers


class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializers


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers


class AbogadoViewSet(viewsets.ModelViewSet):
    queryset = Abogado.objects.all()
    serializer_class = AbogadoSerializers


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        user = request.user
        if user.groups.filter(name='cliente').exists():
            return redirect(to='hola')

        return redirect(to='ahome')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": registrarForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"],
                    password=request.POST["password1"],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'])
                group = Group.objects.get(name='cliente')
                user.groups.add(group)
                user.save()
                login(request, user)
                user = request.user
                if user.groups.filter(name='cliente').exists():
                    return redirect(to='hola')
                else:
                    return redirect(to='ahome')
            except IntegrityError:
                return render(request, 'signup.html', {"form": registrarForm, "error": "Usuario ya existe."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Contrasenias no coinciden."})

def signup2(request):
    if request.method == 'GET':
        return render(request, 'signup2.html', {"form": registrarForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"],
                    password=request.POST["password1"],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'])
                group = Group.objects.get(name='abogado')
                user.groups.add(group)
                user.save()
                login(request, user)
                user = request.user
                if user.groups.filter(name='abogado').exists():
                    return redirect(to='ahome')
                else:
                    return redirect(to='hola')
            except IntegrityError:
                return render(request, 'signup2.html', {"form": registrarForm, "error": "Usuario ya existe."})

        return render(request, 'signup2.html', {"form": UserCreationForm, "error": "Contrasenias no coinciden."})

@login_required
def signout(request):
    logout(request)
    return redirect(to='signin')

@login_required
# @permission_required(user.view_user)
def ahome(request):
    clientes = User.objects.filter(groups=1)
    data = {
        'clientes': clientes
    }
    user = request.user
    if user.groups.filter(name='cliente').exists():
            return redirect(to='hola')
    return render(request, 'ahome.html', data)





# @login_required
# def agregarcli(request, username=None):
#     current_user = request.user
#     if username and username != current_user.username:
#         user = Cliente.objects.get(user=username)
#     else:
#         user = current_user
    
#     return render(request, 'agregarcli.html', {'user': user})


@login_required
def miperfil(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
    return render(request, 'miperfil.html', {'user': user})

@login_required
def perfilcli(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
    return render(request, 'perfilcli.html', {'user': user})


@login_required
def modificarcliente(request):
    if request.method == 'POST':
        cform = agregarcliFrom(request.POST, request.FILES, instance=request.user.cliente)
        if cform.is_valid():
            cform.save()
            messages.success(request, "Perfil modificado Correctamente")
            user = request.user
            if user.groups.filter(name='cliente').exists():
                return redirect(to='hola')
            else:
                return redirect(to='ahome')
    else:
        cform = agregarcliFrom(instance=request.user)
    data = {'cform':cform}    
    return render(request, 'modificarperfil.html',data)


@login_required
def modificarabogado(request):
    if request.method == 'POST':
        aform = agregaraboFrom(request.POST, request.FILES, instance=request.user.abogado)
        if aform.is_valid():
            aform.save()
            messages.success(request, "Perfil modificado Correctamente")
            user = request.user
            if user.groups.filter(name='cliente').exists():
                return redirect(to='hola')
            else:
                return redirect(to='ahome')
    else:
        aform = agregaraboFrom(instance=request.user)
    data = {'aform':aform}
    return render(request, 'modificarperfila.html',data)

# @login_required
# def modificarusuario(request, username):
#     user = get_object_or_404(User, username=username)
#     data = {
#         'form': registrarForm(instance=user)
#     }

#     if request.method == 'POST':
#         formulario = registrarForm(
#             data=request.POST, instance=user, files=request.FILES)
#         if formulario.is_valid():
#             formulario.save()
#             messages.success(request, "Cliente modificado Correctamente")
#             return redirect(to='ahome')
#         data['form'] = formulario
#     return render(request, 'modificarcli.html', data)

@login_required
def hola(request):
    return render(request, 'hola.html')

@login_required
def uploadFile(request):
    documents = Documento.objects.filter(user=request.user)
    data = {
        'documents':documents
    }
    if request.method =='POST':
        titulo = request.POST["fileTitle"]
        documento = request.FILES["uploadedFile"]
        documento = Documento(
            titulo = titulo,
            documento = documento
        )
        documento.user =request.user
        documento.save()
        user = request.user
        if user.groups.filter(name='abogado').exists():
            return redirect(to='signin')
        return render(request, "cargarDoc.html", data)
    return render(request, "cargarDoc.html",data)
    

@login_required
def eliminardoc(request,id):
    doc = get_object_or_404(Documento, id=id)
    doc.delete()
    messages.success(request, "Documento eliminado correctamente")
    return redirect(to='cargarDoc')


# @login_required
# def documentoscli(request):
#     user = request.user
#     if user.groups.filter(name='cliente').exists():
#         return render(request, 'documentoscli.html')

def documentoscli(request, username):
    current_user = request.user
    if username and username != current_user.username:
        user = Documento.objects.get(user=username)
        print(user)
    else:
        user = current_user
    return render(request, 'documentoscli.html', {'user': user})

    
