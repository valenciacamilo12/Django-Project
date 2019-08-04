from django import forms
from apps.empleados.models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado

        fields = [
            'codigo_empleado',
            'nombre',
            'apellido1',
            'apellido2',
            'extencion',
            'email',
            'codigo_oficina',
            'codigo_jefe',
            'puesto',
            'oficina',
        ]

        labels = {
            'codigo_empleado':'Codigo Empleado',
            'nombre':'Nombre',
            'apellido1':'Apellido 1',
            'apellido2':'Apellido 2',
            'extencion':'Extencion',
            'email':'Email',
            'codigo_oficina':'Codigo Oficina',
            'codigo_jefe': 'Codigo Jefe',
            'puesto':'Puesto',
            'oficina':'Oficina',
        }

        widgets = {
            'codigo_empleado': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido1': forms.TextInput(attrs={'class':'form-control'}),
            'apellido2': forms.TextInput(attrs={'class':'form-control'}),
            'extencion': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'codigo_oficina': forms.TextInput(attrs={'class':'form-control'}),
            'codigo_jefe': forms.TextInput(attrs={'class':'form-control'}),
            'puesto': forms.TextInput(attrs={'class':'form-control'}),
            'oficina': forms.Select(attrs={'class':'form-control'}),

        }