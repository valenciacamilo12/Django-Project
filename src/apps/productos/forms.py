from django import forms
from apps.productos.models import Producto,GamaProductos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
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
            'nombre': forms.TextInput(attrs = {'class':'form-control'}),
            'dimensiones': forms.TextInput(attrs = {'class':'form-control'}),
            'proveedor': forms.TextInput(attrs = {'class':'form-control'}),
            'descripcion': forms.TextInput(attrs = {'class':'form-control'}),
            'cantidad_stock': forms.TextInput(attrs = {'class':'form-control'}),
            'precio_venta': forms.TextInput(attrs = {'class':'form-control'}),
            'precio_proveedor': forms.TextInput(attrs = {'class':'form-control'}),
            'gama_producto': forms.Select(attrs = {'class':'form-control'}),
        }

class GamaProductoForm(forms.ModelForm):
    class Meta:
        model = GamaProductos

        fields = [
            'gama',
            'descripcion_texto',
            'descripcion_html',
        ]


        labels = {
            'gama':'Gama',
            'descripcion_texto':'Descripcion Texto',
            'descripcion_html':'Descripcion Html',
        }

        widgets = {
            'gama': forms.TextInput(attrs = {'class':'forms-control'}),
            'descripcion_texto': forms.TextInput(attrs = {'class':'form-control'}),
            'descripcion_html': forms.TextInput(attrs = {'class':'form-control'}),
        }