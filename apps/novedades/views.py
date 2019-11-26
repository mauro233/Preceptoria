from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse_lazy
from django.views.generic.edit import (
	CreateView,
    UpdateView,
    DeleteView
)

from .models import Anuncio
from .serializers import AnuncioSerializer
from rest_framework import generics


class ListAnuncioView(ListView):
	model = Anuncio
	queryset = Anuncio.objects.all()
	template_name = 'novedades/index.html'
	context_object_name = 'anuncios'

class DetailAnuncioView(DetailView):
	model = Anuncio
	template_name = 'novedades/detalle_anuncio.html'
	context_object_name = 'anuncio'


class AnuncioList(generics.ListAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

class CreateAnuncioView(SuccessMessageMixin, CreateView):
	model = Anuncio
	success_menssage = 'Anuncio Creado con Exito'
	fields = ['titulo','descripcion','dirigido','tipo']
	template_name = 'novedades/anuncio_create.html'
	success_url = reverse_lazy('anuncios:list_anuncios') 

class UpdateAnuncioView(SuccessMessageMixin, UpdateView):
	model = Anuncio
	success_menssage = 'Anuncio Actualizado con Exito'
	fields = ['titulo','descripcion','dirigido','tipo']
	template_name = 'novedades/anuncio_update.html'
	success_url = reverse_lazy('anuncios:list_anuncios')  

class DeleteAnuncioView(SuccessMessageMixin,DeleteView):
	model = Anuncio
	success_menssage='Anuncio Borrado con exito'
	template_name = 'novedades/delete_anuncio.html'
	success_url = reverse_lazy('anuncios:list_anuncios')

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Anuncio, id=id_)

