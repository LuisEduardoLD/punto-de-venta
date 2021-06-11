from django import forms

from .models import TBL_Pedidos


class pedidosForm(forms.ModelForm):
    class Meta:
        model = TBL_Pedidos

        fields = [
            'mesa', 'id_producto', 'id_combo', 'id_promocion', 'id_alimento', 'entregado', 'cantidad',
            'pagado', 'active'
        ]

