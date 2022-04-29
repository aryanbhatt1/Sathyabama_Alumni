from django.urls import path, include
from . import views
from django.conf import settings
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.AlumniSignUp, name='alumnisignup'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('events', views.Event, name='events'),
    path('events/alumnimeetevent/<id>', views.EventsPage, name='viewevent'),
    path('admin/addevent', views.EventFormView, name='addEvent'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('viewEvents', views.ViewEvents, name='viewEvents'),
    path('deleteEvents/<id>', views.deleteEvents, name='deleteEvents'),
    path('users/', include('django.contrib.auth.urls')),
    path('viewUsers/', views.viewUsers, name='viewUsers'),
    path('accounts/login/', views.UserLogin, name='login'),
    path('signup/UserDetails/<id>', views.UserDetailsForm, name='userDetails'),
    path('contact', views.contact, name='contact'),
    path('viewEvent/<id>', views.EventView, name='viewEvent'),
    path('approveUsers', views.approveUsers, name='approveUsers'),
    path('approve/<id>', views.ApproveUser, name='userApprove'),
    path('deleteUser/<id>', views.deleteUser, name='deleteUser'),
    path('manageUser/<id>', views.view_user_info, name='viewUserInfo')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

