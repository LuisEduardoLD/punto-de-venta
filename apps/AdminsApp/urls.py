from django.urls import path
from .views import *

app_name = 'admin'

urlpatterns = [
    path('', home, name='home'),

    # URLs para empleados
    path('puestos/', puestos, name='puestos'),
    path('empleados/<str:tipo>', empleados, name='empleados'),
    path('actualizarempleado/<int:pk>', actualizarempleado, name='actualizarempleado'),
    path('eliminarempleado/', eliminarempleado, name='eliminarempleado'),

    # URLs para Insumos
    path('insumos/', insumos, name='insumos'),

    # URLs para menu
    path('menu/', menu, name='menu'),

    # URLs para menu
    path('promociones/', promociones, name='promociones'),
]
