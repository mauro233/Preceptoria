from django.urls import path, include
from .views import(
	ListFaltaProfesorView
)

app_name= 'falta_profesor'
urlpatterns = [
    path('', ListFaltaProfesorView.as_view(), name='list'),
]
