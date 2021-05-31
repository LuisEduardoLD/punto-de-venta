from django.shortcuts import render, redirect
from .forms import *
from apps.EmpleadosApp.models import *
from ..CajerosApp.forms import cajasForm, tipo_operacion_form, denominacionForm, registro_Cajas_Form
from ..CajerosApp.models import CAT_Cajas, CAT_Denominacion, CAT_Tipo_Operacion
from ..Producto.forms import alimentosForm, combosForm, ProductosForm, promosForm, proveedoresForm
from ..Producto.models import CAT_Producto, CAT_ALIMENTOS, TBL_COMBOS, TBL_Promociones, Cat_Proveedores


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


# <!--------------------- Aqui empiezan las URLs para el manejo de la parte de las promociones ---------->

def promociones(req):
    return render(req, 'Admins/Promociones/index.html')

# <!--------------------- Aqui terminan las URLs para el manejo de la parte de las promociones ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de los pedidos del mesero ---------->

def pedidos(req):
    return render(req, 'Admins/Empleados/meseros/pedidos.html')

# <!--------------------- Aqui terminan las URLs para el manejo de la parte de las promociones ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de las cajas ---------->

def cajas(req):
    form = cajasForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:cajas')
    else:
        query = CAT_Cajas.objects.all()

        params = {
            'query': query,
            'form': form
        }
        return render(req, 'Admins/Empleados/cajeros/cajas.html', params)


# <!--------------------- Aqui terminan las URLs para el manejo de las cajas ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de los tipos de operacion ---------->

def tipo_operacion(req):
    form = tipo_operacion_form(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:tipo_operacion')
    else:
        query = CAT_Tipo_Operacion.objects.all()
        params = {
            'query': query,
            'form': form
        }
        return render(req, 'Admins/Empleados/cajeros/tipos_operacion.html', params)


# <!--------------------- Aqui terminan las URLs para el manejo de los tipos de operacion ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de las denominaciones ---------->

def denominacion(req):
    form = denominacionForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:denominacion')
    else:
        query = CAT_Denominacion.objects.all()

        params = {
            'query': query,
            'form': form
        }
        return render(req, 'Admins/Empleados/cajeros/denominaciones.html', params)


# <!--------------------- Aqui terminan las URLs para el manejo de las denominaciones ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de las denominaciones ---------->

def registro_cajas(req):
    form = registro_Cajas_Form(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:registro_cajas')
    else:
        query = CAT_Cajas.objects.all()
        params = {
            'query': query,
            'form': form
        }
        return render(req, 'Admins/Empleados/cajeros/uso_cajas.html', params)


# <!--------------------- Aqui terminan las URLs para el manejo de las denominaciones ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de los alimentos ---------->

def alimentos(req):
    form = alimentosForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:alimentos')
    else:
        query = CAT_ALIMENTOS.objects.all()
        params = {
            'query': query,
            'form': form
        }
        return render(req, 'Admins/alimentos/index.html', params)


# <!--------------------- Aqui terminan las URLs para el manejo de las denominaciones ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de los combos ---------->

def combos(req):
    form = combosForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        combo = form.save(commit=False)
        combo.save_m2m()
        return redirect('admin:combos')
    else:
        validador_productos = CAT_Producto.objects.all().count()
        query = TBL_COMBOS.objects.all()
        print(query)
        params = {
            'query': query,
            'form': form,
            'validador': validador_productos
        }
        return render(req, 'Admins/alimentos/combos.html', params)


# <!--------------------- Aqui terminan las URLs para el manejo de los combos ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de los combos ---------->

def productos(req):
    form = ProductosForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:productos')
    else:
        query = CAT_Producto.objects.all()
        params = {
            'query': query,
            'form': form,
        }
        return render(req, 'Admins/alimentos/productos.html', params)


# <!--------------------- Aqui terminan las URLs para el manejo de los combos ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de las promociones ---------->

def promociones(req):
    form = promosForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:promos')
    else:
        query = TBL_Promociones.objects.all()
        print(query)
        params = {
            'query': query,
            'form': form,
        }
        return render(req, 'Admins/alimentos/promociones.html', params)


# <!--------------------- Aqui terminan las URLs para el manejo de las promociones ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de las promociones ---------->

def proveedores(req):
    form = proveedoresForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:proveedores')
    else:
        query = Cat_Proveedores.objects.all()
        params = {
            'query': query,
            'form': form,
        }
        return render(req, 'Admins/alimentos/proveedores.html', params)


# <!--------------------- Aqui terminan las URLs para el manejo de las promociones ---------->
