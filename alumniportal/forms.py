import email
from statistics import mode
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateField, NumberInput
from .models import Events, FacultyUser
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

class FacultyUserForm(ModelForm):
    class Meta:
        model=FacultyUser
        fields = ('first_name', 'last_name', 'gender', 'profile_image',
                  'YearOfCompletion', 'EmploymentType', 'present_employer_name',
                  'designation', 'country', 'state', 'city', 'special_achievement',
                  'present_status', 'university_name', 'country_university',
                  'state_university', 'city_university', 'country_current',
                  'state_current', 'city_current', 'phone1', 'phone2',
                  'mobile', 'email_id')
