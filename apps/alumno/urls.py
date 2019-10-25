from django.urls import path
from .views import SignUpView, SignInView, SignOutView

app_name='sesion'
urlpatterns = [
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('incia-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
]