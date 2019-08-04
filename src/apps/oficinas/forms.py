from django import forms
from apps.oficinas.models import Oficinas

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficinas

        fields = [
            'codigo_oficina',
            'ciudad',
            'pais',
            'region',
            'codigo_postal',
            'telefono',
            'linea_direccion1',
            'linea_direccion2',
        ]

        labels = {
            'codigo_oficina':'Codigo Oficina',
            'ciudad':'Ciudad',
            'pais':'Pais',
            'region':'Region',
            'codigo_postal':'Codigo Postal',
            'telefono':'Telefono',
            'linea_direccion1':'Linea Direccion 1',
            'linea_direccion2':'Linea Direccion 2',
        }


        widgets = {
            'codigo_oficina': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs = {'class':'form-control'}),
            'pais': forms.TextInput(attrs ={'class':'form-control'}),
            'region': forms.TextInput(attrs ={'class':'form-control'}),
            'codigo_postal': forms.TextInput(attrs ={'class':'form-control'}),
            'telefono':forms.TextInput(attrs ={'class':'form-control'}),
            'linea_direccion1': forms.TextInput(attrs ={'class':'form-control'}),
            'linea_direccion2': forms.TextInput(attrs ={'class':'form-control'}),
        }