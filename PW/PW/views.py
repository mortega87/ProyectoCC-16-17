# -*- coding: UTF-8 -*-
import os

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *

from django import forms

from pymongo import MongoClient
from PW import forms
import pymongo


from django.http import JsonResponse

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.pw

usuarios=db['usuarios']
disco=db['disco']
comentario=db['comentarios']

# Create your views here.
def index (request):
    data = lista();
    return render(request, 'index.html',{'discos_index':lista()})


def administrar (request):
    return render(request, 'administrador.html')

def formulario (request):
	if request.method=='POST':
		x=db.usuarios.find_one({"Usuario": request.POST['username']})
		if x==None:
			request.session["username"]=request.POST['username']
			db.usuarios.insert({
				"Nombre": request.POST['nombre'],
				"Apellidos": request.POST['apellidos'],
				"Usuario": request.POST['username'],
				"Password": request.POST['contrasenia'],
				"Direccion":request.POST['direccion'],
				"Ciudad":request.POST['ciudad'],
              	"Codigo Postal":request.POST['direccion_postal'],
				"Provincia":request.POST['provincia'],
				"Email": request.POST['email'],
				"Dni": request.POST['dni'],
				"Visa": request.POST['tarjeta'],
				"Observaciones":request.POST['comentarios'],
				})
			return render(request, 'index.html',{'discos_index':lista()})

	return render(request,'formulario.html')

'''formulario_disco corresponde al formulario del forms'''
def inserta_disco (request):
    if request.method=='POST':
        disc_form=formulario_disco(request.POST,request.FILES)
        if request.FILES:
            url='/static/img/' + request.FILES['portada'].name
            imagenes_discos(request)
        else:
            url=''

        db.disco.insert({
        "Artista":request.POST['artista'],
        "Titulo":request.POST['titulo'],
        "Estilo":request.POST['estilo'],
        "Imagen":url,
        })
    return render(request, 'administrador.html',{'disc_form':formulario_disco})

'''Funcion de busqueda de discos por Estilo'''
def lista_disco(discos):
    genero=db.disco.find({"Estilo":discos},{"_id":0, "Artista":1, "Titulo":1, "Estilo":1, "Imagen":1})
    discos=[]
    for doc in genero:
        discos.append(doc)
    return discos

'''Funcion de busqueda por titulo de disco'''
def lista_disco_titulo(disco):
    titulo=db.disco.find({"Titulo":disco},{"_id":0, "Artista":1, "Titulo":1, "Estilo":1, "Imagen":1})
    discos=[]
    for doc in titulo:
        discos.append(doc)
    return discos

'''Funcion de busqueda de todos los discos contenidos en la bd'''
def lista():
    x=db.disco.find({},{"_id":0, "Artista":1, "Titulo":1, "Estilo":1, "Imagen":1})
    discos=[]
    for doc in x:
        discos.append(doc)
    return discos

'''busqueda por genero: mostrardisc almacena en la variable genero el Estilo que tenemos en el menu de secciones.'''
def mostrar_genero(request):
    mostrardisc=request.GET.get('genero',None)
    if mostrardisc!=None:
        x=db.disco.find({"Estilo":mostrardisc})
        if x!=None:
            y=lista_disco(mostrardisc)
            return render(request, 'rock.html',{'datosdisco':lista_disco(mostrardisc)})


'''busqueda por titulo: primer GET para la url y segundo para el identificador titulo de html'''
def mostrar_disco_titulo(request):
    mostrardisc=request.GET.get('titulo',None)
    if mostrardisc!=None:
        x=db.disco.find({"Titulo":mostrardisc})
        if x!=None:
            y=lista_disco_titulo(mostrardisc)
            return render(request, 'disco.html',{'com':lista_comentarios(),'datosdisco2':lista_disco_titulo(mostrardisc),'lista1':lista()})

'''busqueda para mostrar los comentarios'''
def lista_comentarios():
    x=db.comentarios.find({},{"_id":0,"Usuario":1,"Titulo":1,"Comentario":1})
    lc=[]
    for doc in x:
        lc.append(doc)

    return lc


def imagenes_discos(request):
	directorio ='PW/static/img/'
	fichero = request.FILES['portada']
	if not os.path.isdir(directorio):
		os.mkdir(directorio)
	with open(directorio + fichero.name,'wb+') as destination :
		for chunk in fichero.chunks():
			destination.write(chunk)


def comentar (request):
    return render(request, 'comentar.html')

def reg_comentario(request):

    if request.method=='POST':
        db.comentarios.insert({
        "Usuario":request.POST['usuario_comentario'],
        "Titulo":request.POST['titulo_disco'],
        "Comentario":request.POST['contenido_comentario'],
        })
    return render(request, 'index.html',{'discos_index':lista()})



def login(request):
	if request.method=='POST':
		x = db.usuarios.find_one({"Usuario": request.POST['username']})
		if x != None:
			if x[u'Password'] == request.POST['contrasenia']:
				request.session['username'] = request.POST['username']
				return render(request, 'index.html',{'discos_index':lista()})
			else:
				return render(request, 'index.html',{'discos_index':lista()})
		else:
			return render(request, 'formulario.html')
	return render(request, 'index.html',{'discos_index':lista()})


def logout(request):
	if 'username' in request.session:
		del request.session['username']
	return HttpResponseRedirect('/')
