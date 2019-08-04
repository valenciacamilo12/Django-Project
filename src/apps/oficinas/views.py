from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView
from django.core.urlresolvers import reverse_lazy
from apps.oficinas.models import Oficinas
from apps.oficinas.forms import OficinaForm

class OficinaCreate(CreateView):
    model = Oficinas
    form_class = OficinaForm
    template_name = 'oficinas/cliente_form.html'
    success_url = reverse_lazy('oficinas:oficina_listar')


class OficinaUpdate(UpdateView):
    model = Oficinas
    form_class = OficinaForm
    template_name = 'oficinas/cliente_form.html'
    success_url = reverse_lazy('oficinas:oficina_listar')


class OficinaDelete(DeleteView):
    model = Oficinas
    form_class = OficinaForm
    template_name = 'oficinas/cliente_delete.html'
    success_url = reverse_lazy('oficinas:oficina_listar')


class OficinaList(ListView):
    model = Oficinas
    template_name = 'oficinas/cliente_list.html'