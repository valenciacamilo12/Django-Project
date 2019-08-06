from django import forms
from apps.clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = [
            'codigo_cliente',
            'nombre_cliente',
            'nombre_contacto',
            'apellido_contacto',
            'telefono',
            'fax',
            'linea_direccion1',
            'linea_direccion2',
            'ciudad',
            'region',
            'pais',
            'usuario',
            'password',
            'codigo_postal',
            'limite_credito',
            'empleado',

        ]

        labels = {
            'codigo_cliente':'Codigo Cliente',
            'nombre_cliente':'Nombre Cliente',
            'nombre_contacto':'Nombre Contacto',
            'apellido_contacto':'Apellido Contacto',
            'telefono':'Telefono',
            'fax':'Fax',
            'linea_direccion1':'Linea Direccion 1',
            'linea_direccion2':'Linea Direccion 2',
            'ciudad':'Ciudad',
            'region':'Region',
            'pais':'Pais',
            'usuario':'Usuario',
            'password':'Password',
            'codigo_postal':'Codigo Postal',
            'limite_credito':'limite_credito',
            'empleado':'empleado',
        }


        widgets = {
            'codigo_cliente': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_contacto': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_contacto': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'fax': forms.TextInput(attrs={'class':'form-control'}),
            'linea_direccion1': forms.TextInput(attrs={'class':'form-control'}),
            'linea_direccion2': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'region': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito': forms.TextInput(attrs={'class':'form-control'}),
            'empleado': forms.Select(attrs={'class':'form-control'}),
        }