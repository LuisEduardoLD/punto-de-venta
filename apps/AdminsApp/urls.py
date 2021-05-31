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

    # URLs para ver los pedidos
    path('pedidos', pedidos, name='pedidos'),

    # URLs para ver las cajas
    path('cajas', cajas, name='cajas'),

    # URLs para ver las cajas
    path('tipo_operacion', tipo_operacion, name='tipo_operacion'),

    # URLs para ver las denominaciones
    path('denominacion', denominacion, name='denominacion'),

    # URLs para ver el uso de cajas
    path('registro_cajas', registro_cajas, name='registro_cajas'),

    # URLs para ver el manejo de los alimentos
    path('alimentos', alimentos, name='alimentos'),

    # URLs para ver el manejo de los alimentos
    path('combos', combos, name='combos'),

    # URLs para ver el manejo de los alimentos
    path('productos', productos, name='productos'),

    # URLs para ver el manejo de las promociones
    path('promociones', promociones, name='promos'),

    # URLs para ver el manejo de las promociones
    path('proveedores', proveedores, name='proveedores'),

]
