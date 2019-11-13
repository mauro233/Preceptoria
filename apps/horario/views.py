from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import HorarioConsulta, Horario


class ListHorarioConsultaView(ListView):
	model = HorarioConsulta
	queryset = HorarioConsulta.objects.all()
	template_name = 'horarios_consulta/index.html'
	context_object_name = 'horariosconsultas'

class DetailHorarioConsultaView(DetailView):
	model = HorarioConsulta
	#template_name = 'horario_consulta/detalle_anuncio.html'
	context_object_name = 'detalle_consulta_horario'


class HorarioView(LoginRequiredMixin, ListView):
	model = Horario
	template_name = 'horario/listado.html'
	context_object_name = 'horarios'

class HorarioDetail(LoginRequiredMixin, DetailView):
	model = Horario
	template_name = 'horario/detalle.html'
	context_object_name = 'horario'

class HorarioCreate(LoginRequiredMixin, CreateView):
	model = Horario
	fields= ['nombre', 'turno', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']
	template_name = 'horario/crear.html'
	success_url = reverse_lazy('horarios:listado')

class HorarioUpdate(LoginRequiredMixin, UpdateView):
	model = Horario
	fields= ['nombre', 'año', 'fecha_hora', 'aula', 'profesores']
	template_name = 'horario/modificar.html'
	success_url = reverse_lazy('horarios:listado')

class HorarioDelete(LoginRequiredMixin, DeleteView):
    template_name = 'horario/borrar.html'
    success_url = reverse_lazy('horarios:listado')
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Horario, id=id_)
	
