from django import forms
from apps.EmpleadosApp.models import User, typeUser


class usuariosForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
             'first_name', 'apellido_paterno', 'apellido_materno', 'email', 'id_typoUsuario', 'col', 'calle', 'numero_ext', 'numero_cel', 'fecha_nacimiento', 'username', 'password','is_active'
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class':'form-control col-5',
                    'placeholder':'Nombre (s)',

                    'style': 'margin: 5px'
                }
            ),
            'apellido_paterno': forms.TextInput(
                attrs={
                    'class': 'form-control col-5',
                    'placeholder':'Apellido Paterno',
                    'style': 'margin: 5px'
                }
            ),
            'apellido_materno': forms.TextInput(
                attrs={
                    'class': 'form-control col-5',
                    'placeholder' : 'Apellido Materno',
                    'style': 'margin: 5px'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control col-5',
                    'type': 'email',
                    'placeholder': 'E-mail',
                    'style' : 'margin : 5px; margin-right:20px '
                }
            ),
            'id_typoUsuario': forms.Select(
                attrs={
                    'class': 'form-control col-7',
                    'style': 'margin: 5px',
                    'placeholder' : 'Tipo'
                }
            ),
            'col': forms.TextInput(
                attrs={
                    'class': 'form-control col-5',
                    'placeholder' : 'Colonia',
                    'style': 'margin: 5px'
                }
            ),
            'calle': forms.TextInput(
                attrs={
                    'class': 'form-control col-5',
                    'placeholder' : 'Calle',
                    'style': 'margin: 5px'
                }
            ),
            'numero_ext': forms.TextInput(
                attrs={
                    'class': 'form-control col-5',
                    'placeholder' : 'Numero exterior',
                    'style': 'margin: 5px',
                    'type': 'number'
                }
            ),
            'numero_cel': forms.TextInput(
                attrs={
                    'class': 'form-control col-5',
                    'placeholder' : 'Numero de celular',
                    'style': 'margin: 5px',
                    'type': 'number'
                }
            ),
            'fecha_nacimiento': forms.TextInput(
                attrs={
                    'class': 'form-control col-4',
                    'placeholder' : 'Fecha de nacimiento',
                    'style': 'margin: 5px',
                    'id':'fecha_nac',
                    'type': 'date'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control col-4',
                    'placeholder' : 'Username',
                    'style': 'margin: 5px'
                }
            ),
            'password' : forms.TextInput(
                attrs={
                    'class': 'form-control col-3',
                    'style': 'margin: 5px',
                    'placeholder' : 'Password',
                    'type' : 'password'

                }
                ),

            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'form-control col-3',
                    'style': 'margin: 5px; display: none'
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