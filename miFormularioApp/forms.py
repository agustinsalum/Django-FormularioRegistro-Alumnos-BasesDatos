
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Usuario, Carrera

class MiFormulario(UserCreationForm):
    carrera     = forms.ModelChoiceField(queryset=Carrera.objects.all(), empty_label="Selecciona una carrera")
    email       = forms.EmailField(required=True)
    imagen      = forms.ImageField(required=False)


    class Meta:
        model = User
        fields = ['last_name','first_name', 'email', 'carrera', 'imagen', 'username', 'password1', 'password2' ]
