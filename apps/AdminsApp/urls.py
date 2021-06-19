from django.urls import path
from .views import *

app_name = 'admin'

urlpatterns = [
    path('', home, name='home'),

    # URLs para empleados
    path('puestos/', puestos, name='puestos'),
    path('empleados/<str:tipo>', empleados, name='empleados'),
    path('actualizar_empleado/<int:pk>', actualizar_empleado, name='actualizar_empleado'),
    path('eliminar_empleado/', eliminar_empleado, name='eliminar_empleado'),

    # URLs para ver los pedidos
    path('pedidos', pedidos, name='pedidos'),
    path('actualizar_pedidos/<slug:slug>', pedidos, name='actualizar_pedidos'),

    # URLs para agregar categorias de alimentos
    path('categorias', categorias, name='categorias'),
    path('actualizar_categorias/<slug:slug>', categorias, name='actualizar_categorias'),

    # URLs para ver las cajas
    path('cajas', cajas, name='cajas'),
    path('actualizar_cajas/<slug:slug>', actualizarCajas, name='actualizar_cajas'),
    path('eliminar_cajas/', eliminar_Cajas, name='eliminar_cajas'),

    # URLs para ver las cajas
    path('tipo_operacion', tipo_operacion, name='tipo_operacion'),
    path('actualizar_tipo_operacion/<slug:slug>', actualizarTipo_operacion, name='actualizar_tipo_operacion'),
    path('eliminar_tipo_operacion/', eliminar_Tipo_operacion, name='eliminar_tipo_operacion'),

    # URLs para ver las denominaciones
    path('denominacion', denominacion, name='denominacion'),
    path('actualizar_denominacion/<slug:slug>', actualizarDenominacion, name='actualizar_denominacion'),
    path('eliminar_denominacion/', eliminar_Denominacion, name='eliminar_denominacion'),

    # URLs para ver el uso de cajas
    path('registro_cajas', registro_cajas, name='registro_cajas'),
    path('actualizar_registro_cajas/<slug:slug>', actualizarRegistro_cajas, name='actualizar_registro_cajas'),
    path('eliminar_registro_cajas', eliminar_Registro_cajas, name='eliminar_registro_cajas'),

    # URLs para ver el manejo de los Alimentos
    path('alimentos', alimentos, name='alimentos'),
    path('actualizar_alimentos/<slug:slug>', actualizarAlimentos, name='actualizar_alimentos'),
    path('eliminar_alimentos/', eliminar_Alimentos, name='eliminar_alimentos'),

    # URLs para ver el manejo de los Alimentos
    path('combos', combos, name='combos'),
    path('actualizar_combos/<slug:slug>', actualizarCombos, name='actualizar_combos'),
    path('eliminar_combos/', eliminar_Combos, name='eliminar_combos'),

    # URLs para ver el manejo de los Alimentos
    path('productos', productos, name='productos'),
    path('actualizar_productos/<slug:slug>', actualizarProductos, name='actualizar_productos'),
    path('eliminar_productos/', eliminar_Producto, name='eliminar_productos'),

    # URLs para ver el manejo de las promociones
    path('promociones', promociones, name='promos'),
    path('actualizar_promociones/<slug:slug>', actualizarPromociones, name='actualizar_promos'),
    path('eliminar_promociones/', eliminar_Promocion, name='eliminar_promos'),

    # URLs para ver el manejo de las promociones
    path('proveedores', proveedores, name='proveedores'),
    path('actualizar_proveedores/<slug:slug>', actualizarProveedores, name='actualizar_proveedores'),
    path('eliminar_proveedores/', eliminar_Proveedores, name='eliminar_proveedores'),

]
