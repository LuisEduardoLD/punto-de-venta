from django.shortcuts import render, redirect
from django.contrib import messages
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
        insersion = form.save()
        if insersion:
            messages.success(req, 'Insersion correcta')
            return redirect('admin:puestos')
        else:
            messages.error(req, 'Hubo problemas al realizar la insersion')
            return redirect('admin:puestos')

    params = {
        'form': form,
        'puestos': puestos
    }
    return render(req, 'Admins/Empleados/puestos.html', params)


def empleados(req, tipo):
    form = usuariosForm(req.POST or None)
    if req.method =='post':
        print('entro post', form.is_valid())
    if req.method == 'POST' and form.is_valid():
        print('entro')
        insersion = form.save()
        if insersion:
            messages.success(req, 'Insersion correcta')
            return redirect('admin:empleados', tipo)
        else:
            messages.error(req, 'Hubo problemas al realizar la insersion')
            return redirect('admin:empleados', tipo)
    else:

        try:
            print(tipo)
            empleo = typeUser.objects.get(puesto=tipo[:-1])
            print(empleo)
            empleados = User.objects.filter(id_typoUsuario=empleo.pk)
            params = {
                'form': form,
                'tipo_usuario': tipo,
                'empleados': empleados
            }
            print('1', empleados)
            return render(req, 'Admins/Empleados/empleados.html', params)
            print('2')
        except:
            messages.error(req, 'Primero tienes que agregar puestos de trabajo')
            return redirect('admin:puestos')


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


# <!--------------------- Aqui empiezan las URLs para el manejo de los pedidos del mesero ---------->

def pedidos(req):
    return render(req, 'Admins/Empleados/meseros/pedidos.html')


# <!--------------------- Aqui terminan las URLs para el manejo de la parte de las promociones ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de las cajas ---------->

def cajas(req):
    form = cajasForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        insersion = form.save()
        if insersion:
            messages.success(req, 'Caja agregada con exito')
            return redirect('admin:cajas')
    else:
        query = CAT_Cajas.objects.all()

        params = {
            'query': query,
            'form': form
        }
        return render(req, 'Admins/Empleados/cajeros/cajas.html', params)


def actualizarCajas(req, slug):
    query = CAT_Cajas.objects.get(slug=slug)
    form = cajasForm(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        actualizacion = form.save()
        if actualizacion:
            messages.success(req, 'Actualizacion de la caja')
            return redirect('admin:cajas')
        else:
            messages.error(req, 'Hubo problemas al realizar la actualizacion')
            return redirect('admin:cajas')
    else:
        params = {
            'form': form
        }
        return render(req, 'Admins/Empleados/actualizacion.html', params)


def eliminar_Cajas(req):
    slug = req.POST['slug']
    if req.method == 'POST':
        CAT_Cajas.objects.filter(slug=slug).update(is_active=False)
        return redirect('admin:cajas')


# <!--------------------- Aqui terminan las URLs para el manejo de las cajas ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de los tipos de operacion ---------->

def tipo_operacion(req):
    form = tipo_operacion_form(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:tipo_operacion')
    else:
        query = CAT_Tipo_Operacion.objects.filter(active=True)
        params = {
            'query': query,
            'form': form
        }
        return render(req, 'Admins/Empleados/cajeros/tipos_operacion.html', params)


def actualizarTipo_operacion(req, slug):
    query = CAT_Tipo_Operacion.objects.get(slug=slug)
    form = tipo_operacion_form(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        actualizacion = form.save()
        if actualizacion:
            messages.success(req, 'Actualizacion correcta ',actualizacion.nombre)
            return redirect('admin:tipo_operacion')
        else:
            messages.error(req, 'Hubo problemas al realizar la actualizacion')
            return redirect('admin:tipo_operacion')
    else:
        params = {
            'form': form
        }
        return render(req, 'Admins/Empleados/actualizacion.html', params)


def eliminar_Tipo_operacion(req):
    slug = req.POST['slug']
    if req.method == 'POST':
        CAT_Tipo_Operacion.objects.filter(slug=slug).update(active=False)
        return redirect('admin:tipo_operacion')



# <!--------------------- Aqui terminan las URLs para el manejo de los tipos de operacion ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de las denominaciones ---------->

def denominacion(req):
    form = denominacionForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:denominacion')
    else:
        query = CAT_Denominacion.objects.filter(active=True)

        params = {
            'query': query,
            'form': form
        }
        return render(req, 'Admins/Empleados/cajeros/denominaciones.html', params)


def actualizarDenominacion(req, slug):
    query = CAT_Denominacion.objects.get(slug=slug)
    form = denominacionForm(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        actualizacion = form.save()
        if actualizacion:
            messages.success(req, 'Actualizacion correcta ',actualizacion.nombre)
            return redirect('admin:denominacion')
        else:
            messages.error(req, 'Hubo problemas al realizar la actualizacion')
            return redirect('admin:denominacion')
    else:
        params = {
            'form': form
        }
        return render(req, 'Admins/Empleados/actualizacion.html', params)


def eliminar_Denominacion(req):
    slug = req.POST['slug']
    if req.method == 'POST':
        CAT_Denominacion.objects.filter(slug=slug).update(is_active=False)
        return redirect('admin:denominacion')


# <!--------------------- Aqui terminan las URLs para el manejo de las denominaciones ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de las denominaciones ---------->

def registro_cajas(req):
    form = registro_Cajas_Form(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:registro_cajas')
    else:
        query = CAT_Cajas.objects.filter(active=True)
        params = {
            'query': query,
            'form': form
        }
        return render(req, 'Admins/Empleados/cajeros/uso_cajas.html', params)


def actualizarRegistro_cajas(req, slug):
    query = CAT_Cajas.objects.get(slug=slug)
    form = registro_Cajas_Form(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        actualizacion = form.save()
        if actualizacion:
            messages.success(req, 'Actualizacion correcta ',actualizacion.nombre)
            return redirect('admin:registro_cajas')
        else:
            messages.error(req, 'Hubo problemas al realizar la actualizacion')
            return redirect('admin:registro_cajas')
    else:
        params = {
            'form': form
        }
        return render(req, 'Admins/Empleados/actualizacion.html', params)


def eliminar_Registro_cajas(req):
    slug = req.POST['slug']
    if req.method == 'POST':
        CAT_Cajas.objects.filter(slug=slug).update(is_active=False)
        return redirect('admin:registro_cajas')


# <!--------------------- Aqui terminan las URLs para el manejo de las denominaciones ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de los Alimentos ---------->

def alimentos(req):
    form = alimentosForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:alimentos')
    else:
        query = CAT_ALIMENTOS.objects.filter(active=True)
        params = {
            'query': query,
            'form': form
        }
        return render(req, 'Admins/Alimentos/alimentos_dir/Alimentos.html', params)


def actualizarAlimentos(req, slug):
    query = CAT_ALIMENTOS.objects.get(slug=slug)
    form = alimentosForm(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        actualizacion = form.save()
        if actualizacion:
            messages.success(req, 'Actualizacion correcta ',actualizacion.nombre)
            return redirect('admin:alimentos')
        else:
            messages.error(req, 'Hubo problemas al realizar la actualizacion')
            return redirect('admin:alimentos')
    else:
        params = {
            'form': form
        }
        return render(req, 'Admins/Empleados/actualizacion.html', params)


def eliminar_Alimentos(req):
    slug = req.POST['slug']
    if req.method == 'POST':
        CAT_ALIMENTOS.objects.filter(slug=slug).update(active=False)
        return redirect('admin:alimentos')


# <!--------------------- Aqui terminan las URLs para el manejo de las denominaciones ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de los combos ---------->

def combos(req):
    form = combosForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:combos')
    else:
        validador_productos = CAT_Producto.objects.filter(active=True).count()
        query = TBL_COMBOS.objects.filter(active=True)
        params = {
            'query': query,
            'form': form,
            'validador': validador_productos
        }
        return render(req, 'Admins/Alimentos/combos/combos.html', params)


def actualizarCombos(req, slug):
    query = TBL_COMBOS.objects.get(slug=slug)
    form = combosForm(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        actualizacion = form.save()
        if actualizacion:
            messages.success(req, 'Actualizacion correcta ',actualizacion.nombre)
            return redirect('admin:combos')
        else:
            messages.error(req, 'Hubo problemas al realizar la actualizacion')
            return redirect('admin:combos')
    else:
        params = {
            'form': form
        }
        return render(req, 'Admins/Empleados/actualizacion.html', params)


def eliminar_Combos(req):
    slug = req.POST['slug']
    if req.method == 'POST':
        TBL_COMBOS.objects.filter(slug=slug).update(active=False)
        return redirect('admin:combos')


# <!--------------------- Aqui terminan las URLs para el manejo de los combos ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de los combos ---------->

def productos(req):
    form = ProductosForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:productos')
    else:
        query = CAT_Producto.objects.filter(active=True)
        params = {
            'query': query,
            'form': form,
        }
        return render(req, 'Admins/Alimentos/productos/productos.html', params)


def actualizarProductos(req, slug):
    query = CAT_Producto.objects.get(slug=slug)
    form = ProductosForm(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        actualizacion = form.save()
        if actualizacion:
            messages.success(req, 'Actualizacion correcta ',actualizacion.nombre)
            return redirect('admin:productos')
        else:
            messages.error(req, 'Hubo problemas al realizar la actualizacion')
            return redirect('admin:productos')
    else:
        params = {
            'form': form
        }
        return render(req, 'Admins/Empleados/actualizacion.html', params)


def eliminar_Producto(req):
    slug = req.POST['slug']
    if req.method == 'POST':
        CAT_Producto.objects.filter(slug=slug).update(active=False)
        return redirect('admin:productos')


# <!--------------------- Aqui terminan las URLs para el manejo de los combos ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de las promociones ---------->

def promociones(req):
    form = promosForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:promos')
    else:
        query = TBL_Promociones.objects.filter(active=True)
        params = {
            'query': query,
            'form': form,
        }
        return render(req, 'Admins/Alimentos/promociones/promociones.html', params)


def actualizarPromociones(req, slug):
    query = TBL_Promociones.objects.get(slug=slug)
    form = promosForm(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        actualizacion = form.save()
        if actualizacion:
            messages.success(req, 'Actualizacion correcta ',actualizacion.nombre)
            return redirect('admin:promos')
        else:
            messages.error(req, 'Hubo problemas al realizar la actualizacion')
            return redirect('admin:promos')
    else:
        params = {
            'form': form
        }
        return render(req, 'Admins/Empleados/actualizacion.html', params)


def eliminar_Promocion(req):
    slug = req.POST['slug']
    if req.method == 'POST':
        TBL_Promociones.objects.filter(slug=slug).update(active=False)
        return redirect('admin:promos')


# <!--------------------- Aqui terminan las URLs para el manejo de las promociones ---------->


# <!--------------------- Aqui empiezan las URLs para el manejo de las promociones ---------->

def proveedores(req):
    form = proveedoresForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin:proveedores')
    else:
        query = Cat_Proveedores.objects.filter(active=True)
        params = {
            'query': query,
            'form': form,
        }
        return render(req, 'Admins/Alimentos/proveedores/proveedores.html', params)


def actualizarProveedores(req, slug):
    query = Cat_Proveedores.objects.get(slug=slug)
    form = proveedoresForm(req.POST or None, instance=query)
    if req.method == 'POST' and form.is_valid():
        actualizacion = form.save()
        if actualizacion:
            messages.success(req, 'Actualizacion correcta ',actualizacion.nombre)
            return redirect('admin:proveedores')
        else:
            messages.error(req, 'Hubo problemas al realizar la actualizacion')
            return redirect('admin:proveedores')
    else:
        params = {
            'form': form
        }
        return render(req, 'Admins/Empleados/actualizacion.html', params)


def eliminar_Proveedores(req):
    slug = req.POST['slug']
    if req.method == 'POST':
        Cat_Proveedores.objects.filter(slug=slug).update(active=False)
        return redirect('admin:proveedores')


# <!--------------------- Aqui terminan las URLs para el manejo de las promociones ---------->
