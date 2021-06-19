from django.urls import path
from .views import *

app_name = 'meseros'

urlpatterns = [
    # ver las mesas en las que esta trabajando el mesero
    path('', meseroIndex, name='mesero_home'),

    # ver los pedidos de cada mesa
    path('pedido/<slug:slug>', ver_pedido, name='ver_pedido'),
]
