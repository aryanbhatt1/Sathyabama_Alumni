import email
from statistics import mode
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateField, NumberInput
from .models import Events
from django.contrib.admin import widgets

class AlumniSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EventForm(ModelForm):
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=NumberInput(attrs={'type': 'time'}))
    class Meta:
        model = Events
        fields = ['title', 'date', 'time', 'venue', 'description', 'poster']
