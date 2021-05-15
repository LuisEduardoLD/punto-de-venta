from django import forms
from apps.Insumos.models import Insumos


class insumosForm(forms.ModelForm):
    class Meta:
        model = Insumos
        fields = [
            'nombre', 'descripcion', 'categoria', 'activo'
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
                    'placeholder': 'Ingresa el nombre'
                }
            ),
            'categoria': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingresa el nombre'
                }
            )

        }