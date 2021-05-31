from django.db import models

from apps.EmpleadosApp.models import User


class CAT_Cajas(models.Model):
    sucursal = models.CharField("Sucursal", max_length=255, default='')
    numero_caja = models.IntegerField('Numero de caja')

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'

    def __str__(self):
        return self.sucursal


class CAT_Tipo_Operacion(models.Model):
    nombre = models.CharField("Nombre", max_length=255, default='')
    descripcion = models.CharField("Descripcion", max_length=255, default='')

    class Meta:
        verbose_name = 'Tipo de operacion'
        verbose_name_plural = 'Tipos de operaciones'

    def __str__(self):
        return self.nombre


class CAT_Denominacion(models.Model):
    valor = models.CharField("Valor", max_length=255, default='')
    tipo_moneda = models.CharField("Tipo de moneda", max_length=255, default='')

    class Meta:
        verbose_name = 'Denominacion'
        verbose_name_plural = 'Denominaciones'

    def __str__(self):
        return self.valor


class TBL_Registro_Cajas(models.Model):
    id_caja = models.ForeignKey(CAT_Cajas, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_tipo_operacion = models.ForeignKey(CAT_Tipo_Operacion, on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fecha', auto_now=True)
    id_denominacion = models.ForeignKey(CAT_Denominacion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Registro de caja'
        verbose_name_plural = 'Registro de cajas'

    def __str__(self):
        return self.nombre
