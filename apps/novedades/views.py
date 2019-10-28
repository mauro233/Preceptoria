from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Anuncio
from .serializers import AnuncioSerializer
from rest_framework import generics


class ListAnuncioView(ListView):
	model = Anuncio
	paginate_by = 5
	queryset = Anuncio.objects.all()
	template_name = 'novedades/index.html'
	context_object_name = 'anuncios'

class DetailAnuncioView(DetailView):
	model = Anuncio
	template_name = 'novedades/detalle_anuncio.html'
	context_object_name = 'detalle'


class AnuncioList(generics.ListAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

  

