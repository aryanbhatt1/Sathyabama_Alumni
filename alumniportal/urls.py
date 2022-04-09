from django.urls import path, include
from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('', views.home, name='home'),
    path('alumnisignup', views.AlumniSignUp, name='alumnisignup'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('events', views.Event, name='events'),
    path('events/alumnimeetevent/<id>', views.EventsPage, name='viewevent'),
    path('admin/addevent', views.EventFormView, name='addEvent'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('viewEvents', views.ViewEvents, name='viewEvents'),
    path('deleteEvents/<id>', views.deleteEvents, name='deleteEvents'),
    path('users/', include('django.contrib.auth.urls')),
]
