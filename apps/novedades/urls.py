from django.urls import path, include
from .views import(
	ListAnuncioView,
	DetailAnuncioView,
	AnuncioList,
	CreateAnuncioView,
	DeleteAnuncioView,
	UpdateAnuncioView
)

app_name= 'anuncios'
urlpatterns = [
    path('serializers/', AnuncioList.as_view(), name='novedades'),
	path('', ListAnuncioView.as_view(), name='list_anuncios'),
	path('detalle/<int:pk>/', DetailAnuncioView.as_view(), name='detail_anuncio'),
	path('crear/', CreateAnuncioView.as_view(), name='create_anuncio'),
	path('borrar/<int:id>/', DeleteAnuncioView.as_view(), name='delete_anuncio'),
	path('actualizar/<int:pk>/', UpdateAnuncioView.as_view(), name='update_anuncio')
]


#si quiere ver la api de novedades: localhost:8000/serializers/
