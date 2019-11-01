from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import HorarioConsulta


class ListHorarioConsultaView(ListView):
	model = HorarioConsulta
	queryset = HorarioConsulta.objects.all()
	template_name = 'horarios_consulta/index.html'
	context_object_name = 'horariosconsultas'

class DetailHorarioConsultaView(DetailView):
	model = HorarioConsulta
	#template_name = 'horario_consulta/detalle_anuncio.html'
	context_object_name = 'detalle_consulta_horario'


