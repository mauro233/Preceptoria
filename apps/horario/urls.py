from django.urls import path, include
from .views import(
	ListHorarioConsultaView,
	DetailHorarioConsultaView
)

app_name= 'horarios'
urlpatterns = [
	path('horarios_consulta/', ListHorarioConsultaView.as_view(), name='consulta' ),
	path('<int:pk>/', DetailHorarioConsultaView.as_view())
]