import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from apps.EmpleadosApp.models import User
from apps.Producto.models import CAT_Producto, TBL_COMBOS, TBL_Promociones, CAT_ALIMENTOS


class TBL_Pedidos(models.Model):
    id_producto = models.ForeignKey(CAT_Producto, on_delete=models.CASCADE, null=True, blank=True, default='')
    id_combo = models.ForeignKey(TBL_COMBOS, on_delete=models.CASCADE, null=True, blank=True, default='')
    id_alimento = models.ForeignKey(CAT_ALIMENTOS, on_delete=models.CASCADE, null=True, blank=True, default='')
    id_promocion = models.ForeignKey(TBL_Promociones, on_delete=models.CASCADE, null=True, blank=True, default='')
    entregado = models.BooleanField('Entregado', default=False)
    cantidad = models.IntegerField('Cantidad', default=0)
    created_at = models.DateTimeField('Hora del pedido', auto_now=True)
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.slug


def set_slug_Pedidos(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format('Pedido', str(uuid.uuid4())[:16])
    )

    instance.slug = slug


pre_save.connect(set_slug_Pedidos, sender=TBL_Pedidos)


class TBL_MESA(models.Model):
    id_mesero =models.ForeignKey(User, on_delete=models.CASCADE, related_name='mesero')
    id_cajero =models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default='', related_name='cajero')
    id_pedido = models.ForeignKey(TBL_Pedidos, on_delete=models.CASCADE, blank=True, default='', related_name='pedido')
    numero_mesa = models.IntegerField('Numero de mesa')
    numero_orden = models.CharField('Numero de orden', max_length=255, default='')
    slug = models.CharField('Numero de orden', max_length=255, default='')


def set_TBL_MESA(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format('Pedido', str(uuid.uuid4())[:16])
    )
    orden = slugify(
        '{}-{}'.format('Orden', str(uuid.uuid4())[:16])
    )
    instance.slug = slug
    instance.numero_orden = orden


pre_save.connect(set_TBL_MESA, sender=TBL_MESA)