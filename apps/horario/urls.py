from django.urls import path, include
from .views import(
	ListHorarioConsultaView,
	DetailHorarioConsultaView
)

urlpatterns = [
	path('horarios_consulta/', ListHorarioConsultaView.as_view()),
	path('<int:pk>/', DetailHorarioConsultaView.as_view())
]