from django.urls import path, include
from .views import(
	ListAnuncioView,
	DetailAnuncioView
)

app_name= 'anuncios'
urlpatterns = [
	path('', ListAnuncioView.as_view(), name = 'list_anuncios'),
	path('<int:pk>/', DetailAnuncioView.as_view(), name = 'detail_anuncio')
]