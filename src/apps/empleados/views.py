from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from apps.empleados.models import Empleado
from apps.empleados.forms import EmpleadoForm
from django.core.urlresolvers import reverse_lazy


class EmpleadoCreate(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/cliente_form.html'
    success_url = reverse_lazy('empleados:empleado_listar')


class EmpleadoUpdate(UpdateView):
    model =  Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/cliente_form.html'
    success_url = reverse_lazy('empleados:empleado_listar')


class EmpleadoDelete(DeleteView):
    model =  Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/cliente_delete.html'
    success_url = reverse_lazy('empleados:empleado_listar')


class EmpleadoList(ListView):
    model =  Empleado
    template_name = 'empleados/cliente_list.html'
