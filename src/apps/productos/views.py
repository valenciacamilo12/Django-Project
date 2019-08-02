from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.productos.models import Producto
from apps.productos.forms import ProductoForm


class ProductCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto:producto_listar')



class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto:producto_listar')


class ProductoDelete(DeleteView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_delete.html'
    success_url = reverse_lazy('producto:producto_listar')


class ProductoList(ListView):
    model = Producto
    template_name = 'producto/producto_list.html'