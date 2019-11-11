from django.contrib import admin

from .models import FaltaProfesor

@admin.register(FaltaProfesor)
class FaltaProfesorAdmin(admin.ModelAdmin):
	list_display = ('profesor','materia','curso','fecha','turno') 
	list_filter = ('profesor','materia','curso','fecha','turno')

