from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path('admin/', admin.site.urls),
    path('alumno/', include('apps.alumno.urls')),
    path('', include('apps.novedades.urls')),
    path('horario/', include('apps.horario.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
