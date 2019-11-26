from django.shortcuts import render
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin 
from django.views.generic.edit import (
	CreateView,
    UpdateView,
    DeleteView
)


from .models import(
	FaltaProfesor
)
class ListFaltaProfesorView(SuccessMessageMixin, ListView):
	model = FaltaProfesor
	queryset = FaltaProfesor.objects.all()
	template_name= 'index.html'
	fields = ['profesor', 'materia', 'curso', 'fecha', 'turno']
	context_object_name = 'faltasprofesores'
	

class CreateFaltaProfesorView(SuccessMessageMixin, CreateView):
	model = FaltaProfesor
	success_menssage = 'Falta de Profesor Creada con Exito'
	fields = ['profesor', 'materia', 'curso', 'fecha', 'turno']
	template_name = 'falta_profesor_create.html'
	success_url = reverse_lazy('falta_profesor:list')


class SearchResultFaltaProfesorView(ListView):
	model = FaltaProfesor
	template_name = 'search.html'

	def get_queryset(self):   
		query = self.request.GET.get('q')
		object_list = FaltaProfesor.objects.filter(
			Q(profesor__icontains=query) | Q(materia__icontains=query) | Q(curso__icontains=query) | Q(fecha__icontains=query)
			)
		return object_list