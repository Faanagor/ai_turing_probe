from django.shortcuts import render, HttpResponse
from .forms import RegForm
from .models import Cliente

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)


class ListaClientes(ListView):
    '''Vista para listar los Clientes de la base de datos'''
    template_name = 'clientes_crud/lista-clientes.html'
    model = Cliente
    context_objet_name = 'clientes'

class AddClientes(CreateView):
    '''Vista para crear un nuevo Cliente a la base de datos'''
    template_name = 'clientes_crud/nuevo-cliente.html'
    model = Cliente 
    fields = ["name_client", "email_client", "category", "country", "city", "user_created"]
    success_url = '/'
    context_objet_name = 'clientes'


def cliente_list_view(request):
    cliente_objects = Cliente.objects.all()
    context = {
        'cliente_objects': cliente_objects
    }

    return render(request, "clientes_crud/inicio.html", context)

# def cliente(request):
#     return HttpResponse("<h1>Primer HttpResponse</h1>")

def home(request):
    form = RegForm()
    context = {
        "el_form": form,
    }
    return render(request, "clientes_crud/nuevo-cliente.html", context)
