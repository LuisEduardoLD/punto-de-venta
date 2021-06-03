from django import forms
from apps.EmpleadosApp.models import User, typeUser


class usuariosForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'is_active', 'id_typoUsuario', 'first_name', 'last_name', 'col', 'calle', 'numero_ext', 'numero_cel', 'fecha_nacimiento', 'username'
        ]

        widgets = {
            'id_typoUsuario': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre(s)'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Apellidos'
                }
            ),
            'col': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Colonia'
                }
            ),
            'calle': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Calle'

                }
            ),
            'numero_ext': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Numero exterior',
                    'type': 'number'
                }
            ),
            'numero_cel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Numero de Teléfono (celular)',
                    'type': 'number'
                }
            ),
            'fecha_nacimiento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Nombre de usuario'
                }
            ),

            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class puestoForm(forms.ModelForm):
    class Meta:
        model = typeUser
        fields = [
            'puesto'
        ]

        widgets = {
            'puesto': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingresa el puesto',
                    'onkeyup':'this.value = this.value.toUpperCase()'
                }
            ),
        }