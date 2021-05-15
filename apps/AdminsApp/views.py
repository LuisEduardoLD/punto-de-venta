from django.shortcuts import render, redirect
from .forms import *
from apps.EmpleadosApp.models import *
from apps.Insumos.models import *
from ..Insumos.forms import insumosForm
from ..Productos.forms import menuForm
from ..Productos.models import Productos


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


def actualizar_empleado(req, pk):
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


def eliminar_empleado(req):
    pk = req.POST['pk']
    if req.method == 'POST':
        User.objects.filter(pk=pk).update(is_active=False)
        return redirect('admin:empleados', req.POST['tipo'])


# <!--------------------- Aqui terminan las URLs para el manejo de la parte de los empleados ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de la parte de los insumos ---------->


def insumos(req):
    form = insumosForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:insumos')
    else:
        insumos = Insumos.objects.all()
        params = {
            'insumos': insumos,
            'form': form
        }
        return render(req, 'Admins/Insumos/index.html', params)


def actualizar_insumos(req, pk):
    query = Insumos.objects.get(pk=pk)
    form = insumosForm(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:insumos')
    else:
        params = {
            'form': form
        }
        return render(req, 'Admins/Insumos/actualizacion.html', params)


def eliminar_insumo(req):
    pk = req.POST['pk']
    if req.method == 'POST':
        Insumos.objects.filter(pk=pk).update(activo=False)
        return redirect('admin:insumos')


# <!--------------------- Aqui terminan las URLs para el manejo de la parte de los insumos ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de la parte del menu ---------->


def menu(req):
    form = menuForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:menu')
    else:
        insumos = Productos.objects.all()
        params = {
            'insumos': insumos,
            'form': form
        }
        return render(req, 'Admins/Menu/index.html', params)


def actualizar_menu(req, pk):
    query = Productos.objects.get(pk=pk)
    form = menuForm(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:menu')
    else:
        params = {
            'form': form
        }
        return render(req, 'Admins/Menu/actualizacion.html', params)


def eliminar_menu(req):
    pk = req.POST['pk']
    if req.method == 'POST':
        Productos.objects.filter(pk=pk).update(activo=False)
        return redirect('admin:menu')


# <!--------------------- Aqui terminan las URLs para el manejo de la parte del menu ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de la parte de las promociones ---------->

def promociones(req):
    return render(req, 'Admins/Promociones/index.html')

# <!--------------------- Aqui terminan las URLs para el manejo de la parte de las promociones ---------->
