from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.contrib.auth.models import User
from apps.clientes.models import Cliente
from apps.clientes.forms import ClienteForm
from django.core.urlresolvers import reverse_lazy

class ClienteCreate(CreateView):
    model = User
    template_name = 'clientes/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('productos:producto_listar')


class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:cliente_listar')


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_delete.html'
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:cliente_listar')


class ClienteList(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
