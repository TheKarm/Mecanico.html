from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from rest_framework import viewsets
from .serializers import *
from rest_framework.renderers import JSONRenderer
import requests
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden

# Create your views here.
def user_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def group_required(group_name):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if user_in_group(request.user, group_name):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden('No tienes permiso para acceder a esta página')
        return _wrapped_view
    return decorator
        


#METODOS PARA LISTAR DESDE EL API
def mecanicosapi(request):
    response = requests.get('http://127.0.0.1:8000/api/mecanicos/')
    mecanicos = response.json()

    aux = {
        'lista'  : mecanicos
    }

    return render(request, 'core/mecanicos/crudapi/index.html', aux)

def mecanicodetalle(request, id):
    response = requests.get(f'http://127.0.0.1:8000/api/mecanicos/{id}/')
    mecanico = response.json()

    aux = {
        'mecanico'  : mecanico
    }

    return render(request, 'core/mecanicos/crudapi/detalle.html', aux)

#UTILIZAMOS LOS VIEWSET PARA MANEJAR LAS SOLICITUDES TIPO HTTP (GET, POST, PUT, DELETE)
class TipoMecanicoViewSet(viewsets.ModelViewSet):
    queryset = TipoMecanico.objects.all().order_by('id')
    serializer_class = TipoMecanicoSerializer
    renderer_classes = [JSONRenderer]

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all().order_by('id')
    serializer_class = GeneroSerializer
    renderer_classes = [JSONRenderer]

class MecanicoViewSet(viewsets.ModelViewSet):
    queryset = Mecanico.objects.all().order_by('id')
    serializer_class = MecanicoSerializer
    renderer_classes = [JSONRenderer]

# <-- INICIO DE LA PÁGINA WEB --> #

def index(request):
    return render(request, 'core/index.html')

def aboutus(request):
    return render(request, 'core/aboutus.html')

def account_locked(request):
    return render(request, 'core/account_locked.html')

def contact(request):
    return render(request, 'core/contact.html')

def services(request):
    return render(request, 'core/services.html')

def team(request):
    return render(request, 'core/team.html')

def testimonial(request):
    return render(request, 'core/testimonial.html')

def cart(request):
    return render(request, 'core/cart.html')

def checkout(request):
    return render(request, 'core/checkout.html')

# <-- FIN DE LA PÁGINA WEB --> #


# ----------------------------------------------------------------------- #


# <-- INICIO DEL ADMINISTRADOR --> #
@login_required
def administrador(request):
    return render(request, 'core/administrador/index.html')

# <-- FIN DEL ADMINISTRADOR --> #


# ----------------------------------------------------------------------- #


# <-- INICIO DEL METODO CRUD --> #
def mecanicos (request):
    mecanicos = Mecanico.objects.all()

    paginator = Paginator(mecanicos, 3) #MUESTRA LA CANTIDAD DE MECÁNICOS SELECCIONADOS POR PÁGINA
    page_number = request.GET.get('page') #BUSCA LA PÁGINA
    page_obj = paginator.get_page(page_number)

    aux = {
        'page_obj' : page_obj,
    }

    return render(request, 'core/mecanicos/index.html', aux)

# <-- ADD --> #
@permission_required('core.add_mecanico')
@group_required('Supervisor')
def mecanicosadd (request):
    aux = {
        'form' : MecanicoForm()
    }

    if request.method == 'POST':
        formulario = MecanicoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mecánico creado correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request, "No se pudo crear el mecánico!")

    return render(request, 'core/mecanicos/crud/add.html', aux)

# <-- UPDATE --> #
@permission_required('core.change_mecanico')
def mecanicosupdate (request, id):
    mecanicos = Mecanico.objects.get(id=id)
    aux = {
        'form' : MecanicoForm(instance=mecanicos)
    }

    if request.method == 'POST':
        formulario = MecanicoForm(data=request.POST, instance=mecanicos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, "Mecánico actualizado correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request, "No se pudo actualizar el mecánico!")

    return render(request, 'core/mecanicos/crud/update.html', aux)

# <-- DELETE --> #
@permission_required('core.delete_mecanico')
def mecanicosdelete (request, id):
    mecanico = Mecanico.objects.get(id=id)
    mecanico.delete()

    return redirect(to="mecanicos")


# <-- FIN DEL METODO CRUD --> #


# <-- INICIO DEL REGITRATION --> #

def register(request):
    aux = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            group = Group.objects.get(name='Cliente, Mecanico, Supervisor')
            user.groups.add(group)

            messages.success(request, "Usuario creado correctamente!")
            return redirect(to='administrador')
        else:
            aux['form'] = formulario

    return render(request, 'registration/register.html', aux)

# <-- FIN DEL REGISTRATION --> #