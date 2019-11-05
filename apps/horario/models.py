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
		choices=DIA_CHOICES,
		help_text='Ingrese el dia que se realizan las horas institucionales'
	)
	desde = models.TimeField(
		help_text='Ingrese la hora de inicio de las horas institucionales'
	)
	hasta = models.TimeField(
		help_text='Ingrese la hora de fin de las horas institucionales'
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
	desde_lunes = models.TimeField(
		help_text='Ingrese el dia y el horario de inicio de la clase del lunes',
		blank=True,
		null=True
	)
	hasta_lunes = models.TimeField(
		help_text='Ingrese el dia y el horario de fin de la clase del lunes',
		blank=True,
		null=True
	)
	desde_martes = models.TimeField(
		help_text='Ingrese el dia y el horario de inicio de la clase del martes',
		blank=True,
		null=True
	)
	hasta_martes = models.TimeField(
		help_text='Ingrese el dia y el horario de fin de la clase del martes',
		blank=True,
		null=True
	)
	desde_miercoles = models.TimeField(
		help_text='Ingrese el dia y el horario de inicio de la clase del miercoles',
		blank=True,
		null=True
	)
	hasta_miercoles = models.TimeField(
		help_text='Ingrese el dia y el horario de fin de la clase del miercoles',
		blank=True,
		null=True
	)
	desde_jueves = models.TimeField(
		help_text='Ingrese el dia y el horario de inicio de la clase del jueves',
		blank=True,
		null=True
	)
	hasta_jueves = models.TimeField(
		help_text='Ingrese el dia y el horario de fin de la clase del jueves',
		blank=True,
		null=True
	)
	desde_viernes = models.TimeField(
		help_text='Ingrese el dia y el horario de inicio de la clase del viernes',
		blank=True,
		null=True
	)
	hasta_viernes = models.TimeField(
		help_text='Ingrese el dia y el horario de fin de la clase del viernes',
		blank=True,
		null=True
	)
	horas_institucionales = models.ForeignKey(
		HorasInstitucionales,
		on_delete=models.CASCADE
	)

	class Meta:
		ordering= ['materia']
		verbose_name='horarioconsulta'
		verbose_name_plural = 'horariosconsultas'

	def __str__(self):
		return '(%s, %s)' % (self.materia, self.profesor)

