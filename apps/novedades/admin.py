from django.contrib import admin

from .models import(
	Anuncio
)


@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
	pass
