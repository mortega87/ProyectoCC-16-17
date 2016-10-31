"""PW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from PW import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/',views.login,name='login'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^administrar/',views.administrar,name='administrar'),
    url(r'^inserta_disco/',views.inserta_disco,name='inserta_disco'),
    url(r'^rock/$',views.mostrar_genero,name='rock'),
    url(r'^formulario/',views.formulario,name='formulario'),
    url(r'^disco/',views.mostrar_disco_titulo,name='disco'),
    url(r'^comentar/',views.comentar,name='comentar'),
    url(r'^reg_comentario/',views.reg_comentario,name='reg_comentario'),
    url(r'^admin/', admin.site.urls),
]
