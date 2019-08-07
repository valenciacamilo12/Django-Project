from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.productos.models import Producto,GamaProductos,Pedidos
from apps.productos.forms import ProductoForm,GamaProductoForm,PedidoForm


class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('productos:producto_listar')



class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('productos:producto_listar')


class ProductoDelete(DeleteView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_delete.html'
    success_url = reverse_lazy('productos:producto_listar')


class ProductoList(ListView):
    model = Producto
    template_name = 'producto/producto_list.html'
    paginate_by = 5


#---------------GamaProduct--------------------

class GamaProductoCreate(CreateView):
    model = GamaProductos
    form_class = GamaProductoForm
    template_name = 'producto/gamaproducto_form.html'
    success_url = reverse_lazy('productos:productogama_listar')



class GamaProductoUpdate(UpdateView):
    model = GamaProductos
    form_class = GamaProductoForm
    template_name = 'producto/gamaproducto_form.html'
    success_url = reverse_lazy('productos:productogama_listar')


class GamaProductoDelete(DeleteView):
    model = GamaProductos
    form_class = GamaProductoForm
    template_name = 'producto/gamaproducto_delete.html'
    success_url = reverse_lazy('productos:productogama_listar')



class GamaProductoList(ListView):
    model = GamaProductos
    template_name = 'producto/gamaproducto_list.html'



#Crear Pedidos


class PedidoCreate(CreateView):
    model = Pedidos
    form_class = PedidoForm
    template_name = 'pedidos/pedido_form.html'
    success_url = reverse_lazy('productos:pedido_listar')



class PedidoUpdate(UpdateView):
    model = Pedidos
    form_class = PedidoForm
    template_name = 'pedidos/pedido_form.html'
    success_url = reverse_lazy('productos:pedido_listar')


class PedidoDelete(DeleteView):
    model = Pedidos
    form_class = PedidoForm
    template_name = 'pedidos/pedido_delete.html'
    success_url = reverse_lazy('productos:pedido_listar')



class PedidoList(ListView):
    model = Pedidos
    template_name = 'pedidos/pedido_list.html'
