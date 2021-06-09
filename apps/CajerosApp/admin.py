from django.contrib import admin

from apps.CajerosApp.models import CAT_Cajas, CAT_Tipo_Operacion, CAT_Denominacion, TBL_Registro_Cajas

admin.site.register(CAT_Cajas)
admin.site.register(CAT_Tipo_Operacion)
admin.site.register(CAT_Denominacion)
admin.site.register(TBL_Registro_Cajas)
