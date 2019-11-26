from django.urls import path, include
from .views import(
	ListFaltaProfesorView,
	SearchResultFaltaProfesorView
)

app_name= 'falta_profesor'
urlpatterns = [
    path('', ListFaltaProfesorView.as_view(), name='list'),
    path('search/', SearchResultFaltaProfesorView.as_view(), name='search')
]
