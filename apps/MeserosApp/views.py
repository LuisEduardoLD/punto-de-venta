from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.EmpleadosApp.models import User
from apps.MeserosApp.forms import pedidosForm
from apps.MeserosApp.models import TBL_Pedidos


def meseroIndex(req):
    form = pedidosForm(req.POST or None)
    if req.method == 'POST' and form.is_valid():
        insersion = form.save()
        TBL_Pedidos.objects.filter(pk=insersion.pk).update(id_usuario=req.user.pk)
        return redirect('meseros:mesero_home')
    else:
        query = TBL_Pedidos.objects.all()
        params = {
            'form': form,
            'query': query
        }
        return render(req, 'Empleados/Meseros/index.html', params)
