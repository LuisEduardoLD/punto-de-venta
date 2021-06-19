from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.EmpleadosApp.models import User
from apps.MeserosApp.forms import pedidosForm, mesaForm
from apps.MeserosApp.models import TBL_MESA, TBL_Pedidos


def meseroIndex(req):
    form = mesaForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        pedido = TBL_Pedidos()
        pedido.save()
        print(pedido)
        insersion = form.save(commit=False)
        insersion.id_mesero = User.objects.get(pk=req.user.pk)
        insersion.id_pedido = pedido
        insersion.save()
        return redirect('meseros:mesero_home')
    else:
        query = TBL_MESA.objects.all()
        params = {
            'form': form,
            'query': query
        }
        return render(req, 'Empleados/Meseros/index.html', params)


def ver_pedido(req, slug):
    mesa = TBL_MESA.objects.get(slug=slug)
    form = ''
    params = {
        'form': form,
        'query': mesa.id_pedido
    }
    return render(req, 'Empleados/Meseros/pedidos/index.html', params)
