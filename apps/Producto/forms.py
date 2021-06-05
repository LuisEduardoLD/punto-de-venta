from django import forms
from .models import CAT_Producto, CAT_ALIMENTOS, TBL_COMBOS, TBL_Promociones, Cat_Proveedores


class alimentosForm(forms.ModelForm):
    class Meta:
        model = CAT_ALIMENTOS

        fields = [
            'nombre', 'categoria', 'descripcion', 'precio'
        ]


class combosForm(forms.ModelForm):
    class Meta:
        model = TBL_COMBOS

        fields = [
            'nombre', 'descripcion', 'precio', 'id_estatus', 'id_producto'
        ]

        widgets = {
            'id_producto': forms.SelectMultiple(
                attrs={
                    'class': 'selectpicker'
                }
            ),
        }


class promosForm(forms.ModelForm):
    class Meta:
        model = TBL_Promociones

        fields = [
            'nombre', 'descripcion', 'porcentaje', 'id_estatus'
        ]


class ProductosForm(forms.ModelForm):
    class Meta:
        model = CAT_Producto
        fields = [
            'nombre', 'descripcion', 'categoria', 'activo', 'precio', 'cantidad'
        ]

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la descripcion'
                }
            ),
            'categoria': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingresa el nombre'
                }
            ),

        }


class proveedoresForm(forms.ModelForm):
    class Meta:
        model = Cat_Proveedores

        fields = [
            'razon_social', 'telefono', 'cp', 'calle', 'no_ext', 'no_int', 'correo', 'colonia', 'estado', 'pais'
        ]



