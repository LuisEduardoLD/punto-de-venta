import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from ..EmpleadosApp.models import User

class Cat_Proveedores(models.Model):
    razon_social = models.CharField('Razon social', max_length=255, default='')
    telefono = models.CharField('Telefono', max_length=10, default='')
    cp = models.CharField('Codigo postal', max_length=5, default='')
    calle = models.CharField('Calle', max_length=255, default='')
    no_ext = models.CharField('Numero exterior', max_length=255, default='')
    no_int = models.CharField('Numero interior', max_length=255, default='')
    correo = models.EmailField('Correo electronico', max_length=255, default='')
    colonia = models.CharField('Colonia', max_length=255, default='')
    estado = models.CharField('Estado', max_length=255, default='')
    pais = models.CharField('Pais', max_length=255, default='')
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.razon_social

def set_slug_Proveedores(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format(instance.razon_social, str(uuid.uuid4())[:8])
    )
    instance.slug = slug


pre_save.connect(set_slug_Proveedores, sender=Cat_Proveedores)


class CAT_Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=255, default='')
    descripcion = models.CharField('Descripcion', max_length=255, default='')
    categoria = models.CharField('Categoria', max_length=255, default='')
    activo = models.BooleanField('Activo', default=True)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    cantidad = models.IntegerField('Cantidad', blank=True, null=True)
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre


def set_slug_Producto(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format(instance.nombre, str(uuid.uuid4())[:8])
    )
    instance.slug = slug


pre_save.connect(set_slug_Producto, sender=CAT_Producto)


class TBL_Inventario(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_numero_inventario = models.IntegerField('Numero Inventario',  null=True)
    fecha = models.DateTimeField('Fecha', auto_now=True)
    id_producto = models.ForeignKey(CAT_Producto, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField('Cantidad')
    id_estatus = models.BooleanField('Estado', default=False)
    precio_paquete = models.DecimalField('Precio del paquete', decimal_places=2, max_digits=99999)
    precio_unitario = models.DecimalField('Precio unitario', decimal_places=2, max_digits=99999)
    id_proveedor = models.ForeignKey(Cat_Proveedores, on_delete=models.CASCADE)
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'

    def __str__(self):
        return self.cantidad


def set_slug_Inventario(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format('Inventario', str(uuid.uuid4())[:8])
    )
    instance.slug = slug


pre_save.connect(set_slug_Inventario, sender=TBL_Inventario)


class TBL_COMBOS(models.Model):
    nombre = models.CharField('Nombre', max_length=255, default='')
    descripcion = models.CharField('Descripcion', max_length=255, default='')
    precio = models.DecimalField('Precio', decimal_places=2, max_digits=99999)
    id_estatus = models.BooleanField('Estado', default=True)
    id_producto = models.ManyToManyField(CAT_Producto, verbose_name='Producto')
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Combo'
        verbose_name_plural = 'Combos'

    def __str__(self):
        return self.nombre


def set_slug_COMBOS(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format(instance.nombre, str(uuid.uuid4())[:8])
    )
    instance.slug = slug


pre_save.connect(set_slug_COMBOS, sender=TBL_COMBOS)


class TBL_Promociones(models.Model):
    nombre = models.CharField('Nombre', max_length=255, default='')
    descripcion = models.CharField('Descripcion', max_length=255, default='')
    porcentaje = models.IntegerField('Porcentaje')
    id_estatus = models.BooleanField('Estado', default=True)
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'

    def __str__(self):
        return self.nombre


def set_slug_Promociones(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format(instance.nombre, str(uuid.uuid4())[:8])
    )
    instance.slug = slug


pre_save.connect(set_slug_Promociones, sender=TBL_Promociones)


class CAT_ALIMENTOS(models.Model):
    nombre = models.CharField('Nombre', max_length=255, default='')
    descripcion = models.CharField('Descripcion', max_length=255, default='')
    categoria = models.CharField('Categoria', max_length=255, default='')
    precio = models.DecimalField('Precio', decimal_places=2, max_digits=99999)
    active = models.BooleanField('Activo', default=True)
    slug = models.CharField(max_length=100, null=False, blank=False, unique=True, default='')

    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'

    def __str__(self):
        return self.nombre


def set_slug_ALIMENTOS(sender, instance, *args, **kwargs):
    slug = slugify(
        '{}-{}'.format(instance.nombre, str(uuid.uuid4())[:8])
    )
    instance.slug = slug


pre_save.connect(set_slug_ALIMENTOS, sender=CAT_ALIMENTOS)

