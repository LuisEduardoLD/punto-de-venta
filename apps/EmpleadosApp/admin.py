from django.contrib import admin

# Register your models here.
from apps.EmpleadosApp.models import User,typeUser, registro_Usuarios

admin.site.register(User)
admin.site.register(registro_Usuarios)
admin.site.register(typeUser)