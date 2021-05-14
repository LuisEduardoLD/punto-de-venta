from django import forms
from apps.Productos.models import Productos


class menuForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'nombre', 'descripcion', 'categoria', 'precio', 'activo'
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
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '0.00',
                    'type': 'number',
                    'min': 1,
                    'step': '0.01'
                }
            )

        }