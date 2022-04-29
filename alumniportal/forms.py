import email
from statistics import mode
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateField, NumberInput
from .models import Events, FacultyUser, PresentStatus
from django.contrib.admin import widgets
from django import forms

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

    present_employer_name = forms.CharField(required=False)
    designation = forms.CharField(required=False)
    country = forms.CharField(required=False)
    state = forms.CharField(required=False)
    city = forms.CharField(required=False)
    special_achievement = forms.CharField(required=False)
    present_status = forms.ModelChoiceField(queryset=PresentStatus.objects.all(),required=False)
    university_name = forms.CharField(required=False)
    country_university = forms.CharField(required=False)
    state_university = forms.CharField(required=False)
    city_university = forms.CharField(required=False)
    phone1 = forms.IntegerField(required=False)
    phone2 = forms.IntegerField(required=False)

    class Meta:
        model=FacultyUser
        fields = ('first_name', 'last_name', 'gender', 'profile_image',
                  'YearOfCompletion', 'EmploymentType', 'degree','present_employer_name',
                  'designation', 'country', 'state', 'city', 'special_achievement',
                  'present_status', 'university_name', 'country_university',
                  'state_university', 'city_university', 'country_current',
                  'state_current', 'city_current', 'phone1', 'phone2',
                  'mobile', 'email_id')

class contactForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
