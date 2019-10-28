from rest_framework import serializers
from .models import Anuncio


class AnuncioSerializer(serializers.ModelSerializer):

	class Meta:
		model = Anuncio
		fields = ("fecha", "titulo", "descripcion", "dirigido", "tipo")
	
	