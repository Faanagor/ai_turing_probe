"""ai_turing_probe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#from .views import cliente
from . import views
#from django.contrib import admin
#from django.conf.urls import url
from django.urls import path

app_name= "clientes_crud_app"
urlpatterns = [
    path('clientes/inicio.html', views.cliente_list_view, name='Lista Clientes'),
    #path('', cliente, name='Cliente'),
    path('clientes/lista', views.ListaClientes.as_view(), name='lista-clientes'),
    path('clientes/add', views.AddClientes.as_view(), name='nuevo-cliente'),
]
