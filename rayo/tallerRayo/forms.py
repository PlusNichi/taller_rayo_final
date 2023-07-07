from django import forms

from tallerRayo.models import Atencion, formularioContacto


from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = ['trabajo', 'diagnostico', 'fecha', 'modeloAuto', 'imagenAuto', 'nombreMecanico', 'cliente', 'rutCliente', 'costo', 'garantia']
        labels = {
            'trabajo': 'Trabajo',
            'diagnostico': 'Diagnóstico',
            'fecha': 'Fecha',
            'modeloAuto': 'Modelo del Auto',
            'imagenAuto': 'Imagen del Auto',
            'nombreMecanico': 'Nombre del Mecánico',
            'cliente': 'Cliente',
            'rutCliente': 'RUT del Cliente',
            'costo': 'Costo',
            'garantia': 'Garantía'
        }

class formularioContactoForm(ModelForm):
    class Meta:
        model = formularioContacto
        fields = '__all__'
        labels = {'nombreCliente': 'Nombre cliente', 'correoGmail': 'Correo Gmail', 'marca': 'Marca',
                  'modeloAuto': 'Modelo de auto', 'tipoServicio': 'Tipo de servicio', 'descripcion': 'Descripción'}

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    # Agrega los campos adicionales que necesites

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')