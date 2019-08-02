from django import forms
from apps.productos.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            'codigo_producto',
            'nombre',
            'dimensiones',
            'proveedor',
            'descripcion',
            'cantidad_stock',
            'precio_venta',
            'precio_proveedor',
            'gama_producto',
        ]


        labels = {
            'codigo_producto':'Codigo Producto',
            'nombre':'Nombre',
            'dimensiones':'Dimensiones',
            'proveedor':'Proveedor',
            'descripcion':'Descripcion',
            'cantidad_stock':'Cantidad Stock',
            'precio_venta':'Precio Venta',
            'precio_proveedor':'Precio Proveedor',
            'gama_producto':'Gama Producto',
        }


        widgets = {
            'codigo_producto': forms.TextInput(attrs = {'class':'forms-control'}),
            'nombre': forms.TextInput(attrs = {'class':'form-control'}),
            'dimensiones': forms.TextInput(attrs = {'class':'form-control'}),
            'proveedor': forms.TextInput(atttrs = {'class':'form-control'}),
            'descripcion': forms.TextInput(attrs = {'class':'form-control'}),
            'cantidad_stock': forms.TextInput(attrs = {'class':'form-control'}),
            'precio_venta': forms.TextInput(attrs = {'class':'form-control'}),
            'precio_proveedor': forms.TextInput(attrs = {'class':'form-control'}),
            'gama_producto': forms.Select(attrs = {'class':'form-control'}),
        }

