from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("El usuario debe Ingresar su email")
        if not username:
            raise ValueError("El usuario debe Ingresar su usuario")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class typeUser(models.Model):
    puesto = models.CharField('Puesto de trabajo', max_length=25)

    class Meta:
        verbose_name = 'Tipo de usuario'
        verbose_name_plural = 'Tipos de usuarios'

    def __str__(self):
        return self.puesto


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField('Email', max_length=70, unique=False, default='', blank=True)

    date_joined = models.DateTimeField('Fecha de registro', auto_now_add=True)
    last_login = models.DateTimeField('Ultimo ingreso', auto_now=True)
    is_admin = models.BooleanField('Administrador', default=False)
    is_active = models.BooleanField('Activo', default=True)
    is_staff = models.BooleanField('Staff', default=False)
    is_superuser = models.BooleanField('SuperUsuario', default=False)

    id_typoUsuario = models.ForeignKey(typeUser, on_delete=models.CASCADE, null=True)
    first_name = models.CharField('Nombre', max_length=255)
    last_name = models.CharField('Apellidos', max_length=255)
    col = models.CharField('Colonia', max_length=255)
    calle = models.CharField('Calle', max_length=255)
    numero_ext = models.IntegerField('Numero Exterior')
    numero_cel = models.IntegerField('Celular')
    fecha_nacimiento = models.DateField('Fecha de nacimiento', null=True)
    username = models.CharField('Usuario', unique=True, max_length=25)
    fecha_alta = models.DateField('Fecha de creacion de usuatrio', auto_now_add=True)
    fecha_actualizacion = models.DateField('Fecha de actualizacion de usuatrio', auto_now=True)

    USERNAME_FIELD = 'username'

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class registro_Usuarios(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_entrada = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_salida = models.DateTimeField(auto_now_add=False, blank=True)

    class Meta:
        verbose_name = 'Fecha de inscripcion o salida de usuario'
        verbose_name_plural = 'Fecha de salida o salida de usuario'

    # def __str__(self):
    #     return self.puesto
