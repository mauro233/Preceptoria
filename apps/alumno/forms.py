from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Alumno

class SignUpForm(UserCreationForm):
    primer_nombre = forms.CharField(max_length=140, required=True)
    segundo_nombre = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'primer_nombre',
            'segundo_nombre',
            'password1',
            'password2',
            )
