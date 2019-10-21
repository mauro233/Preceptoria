from django.db import models



class HorarioConsulta (models.Model):
	profesor = models.CharField(
		max_length=50,
		help_text='Ingrese nombre del profesor que dara la clase de consulta'
	)
	materia = models.CharField(
		max_length=20,
		help_text='Ingrese el nombre de la materia o jefatura de lo que se va a dar en la clase de consulta'
	)
	desde = models.DateTimeField(
		help_text='Ingrese el dia y el horario de inicio de la clase'
	)
	hasta = models.DateTimeField(
		help_text='Ingrese el dia y el horario de fin de la clase'
	)

	class Meta:
		ordering= ['-desde']
		verbose_name='horarioconsulta'
		verbose_name_plural = "horariosconsultas"

	def __str__(self):
		return '(%s, %s, %s)' % (self.materia, self.desde, self.hasta)

