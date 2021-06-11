import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from apps.EmpleadosApp.models import User
from apps.Producto.models import CAT_Producto, TBL_COMBOS, TBL_Promociones, CAT_ALIMENTOS


class TBL_Pedidos(models.Model):

    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateTimeField('Fecha', auto_now=True)
    mesa = models.CharField('Mesa', max_length=5, default='')
    numero_orden = models.CharField('Numero de orden', max_length=255, default='')
    id_producto = models.ManyToManyField(CAT_Producto, blank=True, default='')
    id_combo = models.ManyToManyField(TBL_COMBOS, blank=True, default='')
    id_promocion = models.ForeignKey(TBL_Promociones, on_delete=models.CASCADE, blank=True, default='')
    id_alimento = models.ManyToManyField(CAT_ALIMENTOS, blank=True, default='')
    entregado = models.BooleanField('Entregado', default=False)
    cantidad = models.IntegerField('Cantidad')
    pagado = models.BooleanField('Pagado', default=False)
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.mesa

def set_slug_Pedidos(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format('Pedido', str(uuid.uuid4())[:16])
    )
    orden = slugify(
        '{}-{}'.format('#Orden', str(uuid.uuid4())[:16])
    )
    instance.slug = slug
    instance.numero_orden = orden

pre_save.connect(set_slug_Pedidos, sender=TBL_Pedidos)
