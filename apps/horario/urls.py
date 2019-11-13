from django.urls import path, include
from .views import(
	ListHorarioConsultaView,
	DetailHorarioConsultaView,
	HorarioView, HorarioDetail,
	HorarioCreate, HorarioUpdate,
	HorarioDelete

)




app_name= 'horarios'
urlpatterns = [
	path('horarios_consulta/', ListHorarioConsultaView.as_view(), name='consulta' ),
	path('<int:pk>/', DetailHorarioConsultaView.as_view()),

	path ('listado/', HorarioView.as_view(), name='listado'),
	path ('detalle/<int:pk>/', HorarioDetail.as_view(), name='detalle'),
	path ('crear/', HorarioCreate.as_view(), name='crear'),
	path ('modificar/<int:pk>/', HorarioUpdate.as_view(), name='modificar'),
	path ('borrar/<int:id>/', HorarioDelete.as_view(), name='borrar'),

]