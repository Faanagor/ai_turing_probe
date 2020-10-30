from django.contrib import admin
#from django.conf.urls import url
from django.urls import path, include
#from clientes_crud_app import views
from clientes_crud_app.views import cliente_list_view, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', cliente_list_view, name='Lista Clientes'),
    path('', home, name='Home'),
    #path('', include('clientes_crud_app.urls'))
]
