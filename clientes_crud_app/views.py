from django.shortcuts import render, HttpResponse
from .forms import RegForm
from .models import Cliente

def cliente_list_view(request):
    cliente_objects = Cliente.objects.all()
    context = {
        'cliente_objects': cliente_objects
    }

    return render(request, "clientes_crud/inicio.html", context)



def cliente(request):
    return HttpResponse("<h1>Primer HttpResponse</h1>")

def home(request):
    form = RegForm()
    context = {
        "el_form": form,
    }
    return render(request, "home.html", context)
