from django import forms
from apps.EmpleadosApp.models import User, typeUser


class usuariosForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
             'id_typoUsuario', 'email', 'first_name', 'apellido_paterno', 'apellido_materno', 'col', 'calle', 'numero_ext', 'numero_cel', 'fecha_nacimiento', 'username', 'password','is_active'
        ]

        widgets = {
            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'form-control col-3',
                    'style': 'margin: 3px'
                }
            ),
            'id_typoUsuario': forms.Select(
                attrs={
                    'class': 'form-control col-4',
                    'style': 'margin: 3px'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingresa el nombre',
                    'style': 'margin: 3px'
                }
            ),
            'apellido_paterno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Apellido Paterno'
                }
            ),
            'apellido_materno': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control col-4',
                    'type': 'email',
                    'placeholder': 'E-mail'
                }
            ),
            'col': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'calle': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'numero_ext': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number'
                }
            ),
            'numero_cel': forms.TextInput(
                attrs={
                    'class': 'form-control',
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
                    'class': 'form-control'
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