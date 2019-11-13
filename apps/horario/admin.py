from django.contrib import admin

from .models import HorarioConsulta, HorasInstitucionales, Horario, Materia


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


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
    fieldsets = (
        (None, {
            'fields': ('nombre',)
        }
        ),
        ('Dia Lunes', {
            'fields': ('L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7')
        }
        ),
        ('Dia Martes', {
            'fields': ('M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7')
        }
        ),
        ('Dia Miercoles', {
            'fields': ('X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7')
        }
        ),
        ('Dia Jueves', {
            'fields': ('J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7')
        }
        ),
        ('Dia Viernes', {
            'fields': ('V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7')
        }
        ),
    )


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',) 
