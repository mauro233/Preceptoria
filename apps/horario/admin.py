from django.contrib import admin

from .models import HorarioConsulta

@admin.register(HorarioConsulta)
class HorarioConsultaAdmin(admin.ModelAdmin):
    list_display = ('profesor', 'materia', 'desde', 'hasta')
