from django.urls import path
from .views import SignUpView

app_name='sesion'
urlpatterns = [
    path('registrate/', SignUpView.as_view(), name='sign_up'),
]