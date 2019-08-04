from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView
from django.core.urlresolvers import reverse_lazy
from apps.oficinas.models import Oficinas

class OficinaCreate(CreateView):
    model = Oficinas
    class_form = OficinaForm
    template_name = 'oficinas/oficinaa'