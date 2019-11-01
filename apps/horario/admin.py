from django.contrib import admin

from .models import HorarioConsulta, HorasInstitucionales


@admin.register(HorasInstitucionales)
class HorasInstitucionalesAdmin(admin.ModelAdmin):
	list_display = ('dia', 'desde', 'hasta')
	list_filter = ('dia', 'desde', 'hasta')

@admin.register(HorarioConsulta)
class HorarioConsultaAdmin(admin.ModelAdmin):
    list_display = ('profesor', 'materia', 'desde', 'hasta', 'horas_institucionales')
    list_filter = ('profesor', 'materia', 'desde', 'hasta', 'horas_institucionales')
