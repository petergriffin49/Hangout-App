from django import forms
from django.conf import settings
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class SpotForm(forms.ModelForm):

    class Meta:
        model = Spot
        fields = ["spot_name", "spot_description", "spot_latitude", "spot_longitude", "photo"]


