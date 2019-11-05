from django.contrib import admin

from .models import HorarioConsulta, HorasInstitucionales


@admin.register(HorasInstitucionales)
class HorasInstitucionalesAdmin(admin.ModelAdmin):
	list_display = ('dia', 'desde', 'hasta')
	list_filter = ('dia', 'desde', 'hasta')

@admin.register(HorarioConsulta)
class HorarioConsultaAdmin(admin.ModelAdmin):
    list_display = ('profesor', 'materia','horas_institucionales')
    list_filter = ('profesor', 'materia', 'desde_lunes', 'hasta_lunes', 'desde_martes', 'hasta_martes', 'desde_miercoles', 'hasta_miercoles', 'desde_jueves', 'hasta_jueves', 'desde_viernes', 'hasta_viernes','horas_institucionales')
    fieldsets = (
    	(None, {
    		'fields': ('profesor', 'materia', 'horas_institucionales')
    	}
    	),
    	('Dia Lunes', {
    		'fields': ('desde_lunes', 'hasta_lunes')
        }
        ),
    	('Dia Martes', {
    		'fields': ('desde_martes', 'hasta_martes')
        }
        ),
    	('Dia Miercoles', {
    		'fields': ('desde_miercoles', 'hasta_miercoles')
        }
        ),
        ('Dia Jueves', {
    		'fields': ('desde_jueves', 'hasta_jueves')
        }
        ),
    	('Dia Viernes', {
    		'fields': ('desde_viernes', 'hasta_viernes')
        }
        ),
    )