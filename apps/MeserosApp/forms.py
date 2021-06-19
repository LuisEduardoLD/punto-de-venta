from django import forms

from .models import TBL_Pedidos, TBL_MESA


class pedidosForm(forms.ModelForm):
    class Meta:
        model = TBL_Pedidos

        fields = [
            'id_producto', 'id_combo', 'id_promocion', 'id_alimento', 'entregado', 'cantidad','active'
        ]


class mesaForm(forms.ModelForm):
    class Meta:
        model = TBL_MESA

        fields = [
            'numero_mesa'
        ]


class crearPedido(forms.ModelForm):
    class Meta:
        model = TBL_MESA

        fields = [
            'id_mesero', 'id_cajero', 'id_pedido', 'numero_mesa', 'numero_orden'
        ]

