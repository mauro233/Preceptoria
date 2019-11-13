from django.db import models
from django.core.validators import(
	MaxValueValidator,
	MinValueValidator
)


DIRIGIDO_A = [
	('padres', 'Padres'),
	('alumno', 'Alumnos'),
	('publico', 'Publico'),
]

TIPO_ANUNCIO = [
	('importante', 'Importante'),
	('evento', 'Evento'),
	('comunicado', 'Comunicado'),
	('otros', 'Otros'),
]

class Anuncio(models.Model):
	fecha = models.DateField(
		auto_now_add=True,
		help_text='Fecha de publicacion'
	)
	titulo = models.CharField(
		max_length=30,
		help_text='Ingrese el titulo del anuncio'

	)
	descripcion = models.TextField(
		help_text='Ingrese el anuncion que quiere realizar',
		blank=False
	)
	dirigido = models.CharField(
		max_length=7,
		choices=DIRIGIDO_A,
		help_text='Ingrese a las personas a las que va dirigido el anuncio'
	)
	tipo = models.CharField(
		max_length=10,
		choices=TIPO_ANUNCIO,
		help_text='Ingrese el tipo de anuncio que se quiere publicar'
	)

	class Meta:
		ordering= ['-fecha']
		verbose_name='anuncio'
		verbose_name_plural = "anuncios"

	def __str__(self):
		return '(%s, %s)' % (self.titulo, self.fecha)


