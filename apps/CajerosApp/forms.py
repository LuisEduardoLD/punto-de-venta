from django import forms

from .models import User, CAT_Cajas, CAT_Tipo_Operacion, CAT_Denominacion, TBL_Registro_Cajas


class cajasForm(forms.ModelForm):
    class Meta:
        model = CAT_Cajas

        fields = [
            'sucursal', 'numero_caja'
        ]

        widgets = {
            'sucursal': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'numero_caja': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class tipo_operacion_form(forms.ModelForm):
    class Meta:
        model = CAT_Tipo_Operacion

        fields = [
            'nombre', 'descripcion'
        ]


class denominacionForm(forms.ModelForm):
    class Meta:
        model = CAT_Denominacion

        fields = [
            'valor', 'tipo_moneda'
        ]


class registro_Cajas_Form(forms.ModelForm):
    class Meta:
        model = TBL_Registro_Cajas

        fields = [
            'id_caja', 'id_usuario', 'id_denominacion', 'id_tipo_operacion'
        ]