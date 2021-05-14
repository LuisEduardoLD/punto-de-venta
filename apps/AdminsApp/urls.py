from django.urls import path
from .views import *

app_name = 'admin'

urlpatterns = [
    path('', home, name='home'),

    # URLs para empleados
    path('puestos/', puestos, name='puestos'),
    path('empleados/<str:tipo>', empleados, name='empleados'),
    path('actualizar_empleado/<int:pk>', actualizar_empleado, name='actualizarempleado'),
    path('eliminar_empleado/', eliminar_empleado, name='eliminarempleado'),

    # URLs para Insumos
    path('insumos/', insumos, name='insumos'),
    path('actualizar_insumos/<int:pk>', actualizar_insumos, name='actualizarinsumos'),
    path('eliminar_insumo/', eliminar_insumo, name='eliminarinsumo'),

    # URLs para menu
    path('menu/', menu, name='menu'),
    path('actualizar_menu/<int:pk>', actualizar_menu, name='actualizarmenu'),
    path('eliminar_menu/', eliminar_menu, name='eliminarmenu'),

    # URLs para menu
    path('promociones/', promociones, name='promociones'),
]
