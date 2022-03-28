from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alumnisignup', views.AlumniSignUp, name='alumnisignup'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('events', views.Event, name='events'),
    path('events/alumnimeetevent/<id>', views.EventsPage, name='viewevent')
]
