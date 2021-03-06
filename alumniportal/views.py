from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AlumniSignUpForm, EventForm, FacultyUserForm, contactForm
from Sathyabama.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
import datetime

# Create your views here.
def today():
    return datetime.today()


def AlumniSignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        form = User.objects.create_user(username, email, password1)
        form.first_name = first_name
        form.last_name = last_name
        form.email = email
        form.save()
        return redirect('signup/UserDetails/%d' % form.id)
    else:
        form = AlumniSignUpForm()
    return render(request, 'pages/auth/signup.html', {'form': form})


def UserDetailsForm(request, id):
    user_name = User.objects.get(id=id)
    form = FacultyUserForm()
    if request.method == 'POST':
        form = FacultyUserForm(request.POST, request.FILES)
        if form.is_valid():
            user_save = form.save(commit=False)
            print(user_name)
            user_save.user = user_name
            user_save.save()
            return HttpResponseRedirect(reverse('home'))
    context = {
        'form': form
    }
    return render(request, 'pages/auth/alumni_registration_form.html', context=context)


@login_required
def Dashboard(request):
    current_user_image = FacultyUser.objects.values_list('profile_image', flat=True).filter(user=request.user)[0]
    current_user_first_name = request.user.first_name
    current_user_last_name = request.user.last_name
    facultyUser_data = FacultyUser.objects.all()
    events_data = Events.objects.all().order_by('-date_time_upload')


    context = {
        'facultyUser_data':facultyUser_data,
        'events_data':events_data,
        'current_user_image': current_user_image,
        'current_user_first_name': current_user_first_name,
        'current_user_last_name': current_user_last_name,
    }
    return render(request, 'pages/admin/dashboard.html', context)


def Event(request):
    events_queries = Events.objects.all()
    context = {


        'events_queries': events_queries
    }
    return render(request, 'pages/events.html', context=context)


def EventsPage(request, id):
    events_queries = Events.objects.get(id=id)

    context = {
        'events_queries': events_queries,
    }
    return render(request, 'pages/eventsPage.html', context=context)


def UserLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff == True:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Your Username or Password is incorrect or not approved.')
            return redirect('login')

    return render(request, 'pages/auth/login.html')


def home(request):
    overview = Overview.objects.all()
    total = Overview.objects.all().filter(total_text='Total')
    event_queries_upcoming = Events.objects.all()[:3]

    dashboard_context = {

        'event_queries_upcoming': event_queries_upcoming,
        'overview': overview,
        'total': total,
    }

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff == True:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Your Username or Password is incorrect')
            return redirect('login')

    return render(request, 'pages/home.html', context=dashboard_context)


@login_required
def EventFormView(request):
    current_user_image = FacultyUser.objects.all().filter(user=request.user)
    current_user_first_name = request.user.first_name
    current_user_last_name = request.user.last_name

    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event_save = form.save(commit=False)
            event_save.user = request.user
            event_save.user_name = request.user.first_name
            event_save.last_name = request.user.last_name
            event_save.photo = FacultyUser.objects.values_list('profile_image', flat=True).filter(user=request.user)[0]
            event_save.date_time_upload = datetime.datetime.now()
            event_save.save()
            messages.success(request, 'Event Successfully Posted.')
            return HttpResponseRedirect(reverse('addEvent'))

    context = {
        'current_user_image': current_user_image,
        'current_user_first_name': current_user_first_name,
        'current_user_last_name': current_user_last_name,
        'form': form,
    }

    return render(request, 'pages/admin/eventform.html', context=context)


@login_required
def ViewEvents(request):
    current_user_image = FacultyUser.objects.values_list('profile_image', flat=True).filter(user=request.user)[0]
    current_user_first_name = request.user.first_name
    current_user_last_name = request.user.last_name
    events = Events.objects.all().order_by('-date')
    context = {
        'current_user_image': current_user_image,
        'current_user_first_name': current_user_first_name,
        'current_user_last_name': current_user_last_name,
        'events': events
    }
    return render(request, 'pages/admin/viewEvents.html', context=context)


def deleteEvents(request, id=id):
    event = Events.objects.get(id=id)
    event.delete()
    return HttpResponseRedirect(reverse('viewEvents'))


@login_required
def EventView(request, id):
    event = Events.objects.get(id=id)

    context = {
        'event': event,
    }
    return render(request, 'pages/admin/viewEventPage.html', context=context)


@login_required
def viewUsers(request):
    current_user_image = FacultyUser.objects.all().filter(user=request.user)
    current_user_first_name = request.user.first_name
    current_user_last_name = request.user.last_name
    user_list = User.objects.all().filter(is_staff=True)
    user_about = FacultyUser.objects.all()

    final_user_list = []
    for i in user_list:
        for j in user_about:
            if i.username == j.user.username:
                dic = {'username': i.username, 'first_name': i.first_name, 'last_name': i.last_name,
                       'designation': j.EmploymentType, 'email_id': i.email, 'profile_photo': j.profile_image.url,
                       'user_id': i.id, 'user_about_id': None}
                final_user_list.append(dic)

    context = {
        'current_user_image': current_user_image,
        'current_user_first_name': current_user_first_name,
        'current_user_last_name': current_user_last_name,
        'final_user_list': final_user_list,
    }
    return render(request, 'pages/admin/users_list.html', context=context)

def ApproveUser(request, id):
    User.objects.filter(id=id).update(is_staff=True)
    return redirect("approveUsers")

def deleteUser(request, id):
    user=User.objects.get(id=id)
    FacultyUser.objects.filter(user=user).delete()
    user.delete()
    return redirect("viewUsers")

def view_user_info(request, id):
    user=User.objects.get(id=id)
    user_data = FacultyUser.objects.all().filter(user=user)
    current_user_image = FacultyUser.objects.all().filter(user=request.user)
    current_user_first_name = request.user.first_name
    current_user_last_name = request.user.last_name

    context = {
        'user_data':user_data,
        'current_user_image':current_user_image,
        'current_user_first_name':current_user_first_name,
        'current_user_last_name':current_user_last_name,
    }

    return render(request, 'pages/admin/viewuserinfo.html', context=context)

@login_required
def approveUsers(request):
    current_user_image = FacultyUser.objects.all().filter(user=request.user)
    current_user_first_name = request.user.first_name
    current_user_last_name = request.user.last_name
    user_list = User.objects.all().filter(is_staff=False)
    user_about = FacultyUser.objects.all()
    final_user_list = []
    for i in user_list:
        for j in user_about:
            print(final_user_list)
            if i.username == j.user.username:
                dic = {'username': i.username, 'first_name': i.first_name, 'last_name': i.last_name,
                       'designation': j.EmploymentType, 'email_id': i.email, 'profile_photo': j.profile_image.url,
                       'user_id': i.id, 'user_about_id': None}
                final_user_list.append(dic)

    context = {
        'current_user_image': current_user_image,
        'current_user_first_name': current_user_first_name,
        'current_user_last_name': current_user_last_name,
        'final_user_list': final_user_list,
    }
    return render(request, 'pages/admin/approve_user.html', context=context)

def contact(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            subject = "Alumni Contact Form"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                mail = EmailMessage(subject, message, EMAIL_HOST_USER, ['aryanbhatt1002@gmail.com'])
                mail.send()
                messages.success(request, 'Message Sent Successfully.')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("contact")
    form = contactForm()
    context = {
        'form': form
    }
    return render(request, 'pages/contact.html', context=context)
