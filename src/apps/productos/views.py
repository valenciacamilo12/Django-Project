from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.productos.models import Producto


class ProductCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto:producto_crear')