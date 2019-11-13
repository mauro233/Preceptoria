from django.db import models


DIA_CHOICES = (
	('lunes', 'Lunes'),
	('martes', 'Martes'),
	('miercoles', 'Miércoles'),
	('jueves', 'Jueves'),
	('viernes', 'Viernes')
)

TURNO_CHOICES = (
	('mañana', 'Mañana'),
	('tarde', 'Tarde'),
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



class Materia(models.Model):
	curso = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)
	profesor = models.CharField(max_length=50)

	def __str__(self):
		return '%s, %s' % (self.nombre, self.profesor)

class Horario(models.Model):

	nombre = models.CharField(max_length=50)
	turno = models.CharField(max_length=50, choices=TURNO_CHOICES)
	
	L1 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='L1Id', help_text='Seleccione la materia', null=True, blank=True)
	L2 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='L2Id', help_text='Seleccione la materia', null=True, blank=True)
	L3 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='L3Id', help_text='Seleccione la materia', null=True, blank=True)
	L4 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='L4Id', help_text='Seleccione la materia', null=True, blank=True)
	L5 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='L5Id', help_text='Seleccione la materia', null=True, blank=True)
	L6 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='L6Id', help_text='Seleccione la materia', null=True, blank=True)
	L7 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='L7Id', help_text='Seleccione la materia', null=True, blank=True)

	M1 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='M1Id', help_text='Seleccione la materia', null=True, blank=True)
	M2 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='M2Id', help_text='Seleccione la materia', null=True, blank=True)
	M3 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='M3Id', help_text='Seleccione la materia', null=True, blank=True)
	M4 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='M4Id', help_text='Seleccione la materia', null=True, blank=True)
	M5 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='M5Id', help_text='Seleccione la materia', null=True, blank=True)
	M6 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='M6Id', help_text='Seleccione la materia', null=True, blank=True)
	M7 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='M7Id', help_text='Seleccione la materia', null=True, blank=True)

	X1 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='X1Id', help_text='Seleccione la materia', null=True, blank=True)
	X2 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='X2Id', help_text='Seleccione la materia', null=True, blank=True)
	X3 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='X3Id', help_text='Seleccione la materia', null=True, blank=True)
	X4 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='X4Id', help_text='Seleccione la materia', null=True, blank=True)
	X5 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='X5Id', help_text='Seleccione la materia', null=True, blank=True)
	X6 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='X6Id', help_text='Seleccione la materia', null=True, blank=True)
	X7 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='X7Id', help_text='Seleccione la materia', null=True, blank=True)

	J1 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='J1Id', help_text='Seleccione la materia', null=True, blank=True)
	J2 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='J2Id', help_text='Seleccione la materia', null=True, blank=True)
	J3 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='J3Id', help_text='Seleccione la materia', null=True, blank=True)
	J4 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='J4Id', help_text='Seleccione la materia', null=True, blank=True)
	J5 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='J5Id', help_text='Seleccione la materia', null=True, blank=True)
	J6 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='J6Id', help_text='Seleccione la materia', null=True, blank=True)
	J7 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='J7Id', help_text='Seleccione la materia', null=True, blank=True)

	V1 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='V1Id', help_text='Seleccione la materia', default='-', null=True, blank=True)
	V2 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='V2Id', help_text='Seleccione la materia', default='-', null=True, blank=True)
	V3 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='V3Id', help_text='Seleccione la materia', default='-', null=True, blank=True)
	V4 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='V4Id', help_text='Seleccione la materia', default='-', null=True, blank=True)
	V5 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='V5Id', help_text='Seleccione la materia', default='-', null=True, blank=True)
	V6 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='V6Id', help_text='Seleccione la materia', default='-', null=True, blank=True)
	V7 = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='V7Id', help_text='Seleccione la materia', default='-', null=True, blank=True)

	def __str__(self):
		return '%s' % (self.nombre)