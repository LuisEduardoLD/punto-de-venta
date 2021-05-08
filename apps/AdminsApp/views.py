from django.shortcuts import render, redirect
from .forms import *
from apps.EmpleadosApp.models import *


def home(req):
    return render(req, 'Admins/index.html')


# <!--------------------- Aqui empiezan las URLs para el manejo de la parte de los empleados ---------->


def puestos(req):
    form = puestoForm(req.POST or None)
    puestos = typeUser.objects.all()
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:puestos')
    params = {
        'form': form,
        'puestos': puestos
    }
    return render(req, 'Admins/Empleados/puestos.html', params)


def empleados(req, tipo):
    form = usuariosForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:empleados', tipo)
    else:
        empleo = typeUser.objects.get(puesto=tipo[:-1])
        empleados = User.objects.filter(id_typoUsuario=empleo.pk)
        params = {
            'form': form,
            'tipo_usuario': tipo,
            'empleados': empleados
        }

        return render(req, 'Admins/Empleados/empleados.html', params)


def actualizarempleado(req, pk):
    query = User.objects.get(pk=pk)
    form = usuariosForm(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:empleados', req.POST['t'] + 'S')
    else:
        params = {
            'form': form,
            'tipo': str(query.id_typoUsuario)
        }
        return render(req, 'Admins/Empleados/actualizacion.html', params)


def eliminarempleado(req):
    pk = req.POST['pk']
    if req.method == 'POST':
        User.objects.filter(pk=pk).update(is_active=False)
        return redirect('admin:empleados', req.POST['tipo'])


# <!--------------------- Aqui terminan las URLs para el manejo de la parte de los empleados ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de la parte de los insumos ---------->


def insumos(req):
    return render(req, 'Admins/Insumos/index.html')


# <!--------------------- Aqui terminan las URLs para el manejo de la parte de los insumos ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de la parte del menu ---------->


def menu(req):
    pass


# <!--------------------- Aqui terminan las URLs para el manejo de la parte del menu ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de la parte de las promociones ---------->

def promociones(req):
    pass

# <!--------------------- Aqui terminan las URLs para el manejo de la parte de las promociones ---------->
