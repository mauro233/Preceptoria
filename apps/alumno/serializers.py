from rest_framework import serializers
from .models import Alumno


class AlumnoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Alumno
		fields = ("usuario", "nombre", "apellido", "correo")
	
	