from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path('admin/', admin.site.urls),
    path('', include('apps.alumno.urls')),
    path('preceptoria/', include('apps.novedades.urls')),
    path('horario/', include('apps.horario.urls')),
]
