from django.db import models


class Insumos(models.Model):
    nombre = models.CharField('Nombre', max_length=255, default='')
    descripcion = models.CharField('Descripcion', max_length=255, default='')
    categoria = models.CharField('Categoria', max_length=255, default='')
    activo = models.BooleanField('Activo', default=True)