from django.db import models

from apps.EmpleadosApp.models import User
from apps.Producto.models import CAT_Producto, TBL_COMBOS, TBL_Promociones, CAT_ALIMENTOS


class TBL_Pedidos(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # id_tipo_operacion = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fecha', auto_now=True)
    mesa = models.CharField('Mesa', max_length=255, default='')
    numero_orden = models.CharField('Numero de orden', max_length=255, default='')
    id_producto = models.ForeignKey(CAT_Producto, on_delete=models.CASCADE)
    id_combo = models.ForeignKey(TBL_COMBOS, on_delete=models.CASCADE)
    id_promocion = models.ForeignKey(TBL_Promociones, on_delete=models.CASCADE)
    id_alimento = models.ForeignKey(CAT_ALIMENTOS, on_delete=models.CASCADE)
    entregado = models.BooleanField('Entregado', default=False)
    cantidad = models.IntegerField('Cantidad')
    pagado = models.BooleanField('Pagado', default=False)
    active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.mesa
