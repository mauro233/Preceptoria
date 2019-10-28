from django.urls import path
from .views import SignUpView, AlumnoList

app_name='sesion'
urlpatterns = [
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('serializers/', AlumnoList.as_view(), name='alumno'),
]

#si quiere ver la api de alumno: localhost:8000/alumno/serializers/


