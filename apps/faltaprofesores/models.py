from django.db import models

class FaltaProfesor (models.Model):
	profesor = models.CharField(
		max_length=50,
		help_text='Ingrese el nombre del profesor'
	)
	materia = models.CharField(
		max_length=50,
		help_text='Ingrese nombre de la materia'
	)
	curso = models.CharField(
		max_length=50,
		help_text='Ingrese el curso donde va a ocurrir la auscencia'
	)
	fecha = models.DateField(
		help_text='Ingrese fecha que ocurrira la falta del profesor'
	)
	turno = models.CharField(
		max_length=50,
		help_text='Ingrese turno en el que el profesor falta'
	)

	class Meta:
		ordering= ['-fecha']
		verbose_name='faltaprofesor'
		verbose_name_plural='faltasprofesores'

	def __str__(self):
		return '(%s, %s, %s)' % (self.profesor, self.materia, self.curso)

