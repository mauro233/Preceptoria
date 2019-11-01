from django.db import models


DIA_CHOICES = (
	('lunes', 'Lunes'),
	('martes', 'Martes'),
	('miercoles', 'Miércoles'),
	('jueves', 'Jueves'),
	('viernes', 'Viernes')
)

class HorasInstitucionales (models.Model):
	dia = models.CharField(
		'Dia de la Semana',
		max_length=10,
		choices='DIA_CHOICES',
		help_text='Ingrese el dia que se realizan las horas institucionales'
	)
	desde = models.TimeField(
		help_text='Ingrese la hora de inicio de las horas institucionales'
	)
	hasta = models.TimeField(
		help_text='Ingrese la hora de fin de las horas institucionales'
	)

	desde = models.TimeField(
		help_text='Ingresela hora de inicio de las horas institucionales'
	)
	class Meta:
		ordering= ['-desde']
		verbose_name='horainstitucional'
		verbose_name_plural = 'horasinstitucionales'

	def __str__(self):
		return '(%s, %s, %s)' % (self.dia, self.desde, self.hasta)


class HorarioConsulta (models.Model):
	profesor = models.CharField(
		max_length=50,
		help_text='Ingrese nombre del profesor que dara la clase de consulta'
	)
	materia = models.CharField(
		max_length=20,
		help_text='Ingrese el nombre de la materia o jefatura de lo que se va a dar en la clase de consulta'
	)
	desde = models.TimeField(
		help_text='Ingrese el dia y el horario de inicio de la clase'
	)
	hasta = models.TimeField(
		help_text='Ingrese el dia y el horario de fin de la clase'
	)
	horas_institucionales = models.ForeignKey(
		HorasInstitucionales,
		on_delete=models.CASCADE
	)

	class Meta:
		ordering= ['-desde']
		verbose_name='horarioconsulta'
		verbose_name_plural = 'horariosconsultas'

	def __str__(self):
		return '(%s, %s, %s)' % (self.materia, self.desde, self.hasta)

