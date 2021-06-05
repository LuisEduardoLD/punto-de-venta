import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from apps.EmpleadosApp.models import User


class CAT_Cajas(models.Model):
    sucursal = models.CharField("Sucursal", max_length=255, default='')
    numero_caja = models.IntegerField('Numero de caja')
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'

    def __str__(self):
        return self.sucursal


def set_slug_Cajas(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format(instance.sucursal, str(uuid.uuid4())[:8])
    )
    instance.slug = slug


pre_save.connect(set_slug_Cajas, sender=CAT_Cajas)


class CAT_Tipo_Operacion(models.Model):
    nombre = models.CharField("Nombre", max_length=255, default='')
    descripcion = models.CharField("Descripcion", max_length=255, default='')
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Tipo de operacion'
        verbose_name_plural = 'Tipos de operaciones'

    def __str__(self):
        return self.nombre


def set_slug_Tipo_Operacion(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format(instance.nombre, str(uuid.uuid4())[:8])
    )
    instance.slug = slug


pre_save.connect(set_slug_Tipo_Operacion, sender=CAT_Tipo_Operacion)


class CAT_Denominacion(models.Model):
    valor = models.CharField("Valor", max_length=255, default='')
    tipo_moneda = models.CharField("Tipo de moneda", max_length=255, default='')
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Denominacion'
        verbose_name_plural = 'Denominaciones'

    def __str__(self):
        return self.valor


def set_slug_Denominacion(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format(instance.tipo_moneda, str(uuid.uuid4())[:8])
    )
    instance.slug = slug


pre_save.connect(set_slug_Denominacion, sender=CAT_Denominacion)


class TBL_Registro_Cajas(models.Model):
    id_caja = models.ForeignKey(CAT_Cajas, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_tipo_operacion = models.ForeignKey(CAT_Tipo_Operacion, on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fecha', auto_now=True)
    id_denominacion = models.ForeignKey(CAT_Denominacion, on_delete=models.CASCADE)
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Registro de caja'
        verbose_name_plural = 'Registro de cajas'

    def __str__(self):
        return self.nombre


def set_slug_Registro_Cajas(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format('Caja', str(uuid.uuid4())[:8])
    )
    instance.slug = slug


pre_save.connect(set_slug_Registro_Cajas, sender=TBL_Registro_Cajas)
