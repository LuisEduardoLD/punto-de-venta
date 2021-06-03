from django.contrib import admin

from apps.Producto.models import Cat_Proveedores, CAT_Producto, TBL_Inventario, TBL_COMBOS, TBL_Promociones, \
    CAT_ALIMENTOS

admin.site.register(Cat_Proveedores)
admin.site.register(TBL_Inventario)
admin.site.register(CAT_Producto)
admin.site.register(TBL_COMBOS)
admin.site.register(TBL_Promociones)
admin.site.register(CAT_ALIMENTOS)
