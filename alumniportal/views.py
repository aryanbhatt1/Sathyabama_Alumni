from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import *
from .forms import AlumniSignUpForm, EventForm


# Create your views here.
def today():
    return datetime.today()


def AlumniSignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = request.cleaned_data.get['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            return redirect('home')
    else:
        form = AlumniSignUpForm()
    return render(request, 'pages/auth/signup.html', {'form': form})


@login_required
def Dashboard(request):
    current_user_image = FacultyUser.objects.values_list('profile_image', flat=True).filter(user=request.user)[0]
    current_user_first_name = request.user.first_name
    current_user_last_name = request.user.last_name
    print(current_user_image)
    context={
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


def home(request):
    overview = Overview.objects.all()
    total = Overview.objects.all().filter(total_text='Total')
    event_queries_upcoming = Events.objects.filter(date__gte=today()).all()[:3]

    dashboard_context = {

        'event_queries_upcoming': event_queries_upcoming,
        'overview': overview,
        'total': total,
    }

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, "pages/home.html", {
                "message": "Invalid Credentials"
            })

    return render(request, 'pages/home.html', context=dashboard_context)


def EventFormView(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event_save = form.save(commit=False)
            event_save.user = request.user
            event_save.user_name = request.user.first_name
            event_save.last_name = request.user.last_name
            event_save.save()
            return HttpResponseRedirect(reverse('addEvent'))

    context = {
        'form': form,
    }

    return render(request, 'pages/admin/eventform.html', context=context)


def ViewEvents(request):
    events = Events.objects.all().order_by('-date')
    context = {
        'events': events
    }
    return render(request, 'pages/admin/viewEvents.html', context=context)

def deleteEvents(request, id=id):
    event = Events.objects.get(id=id)
    event.delete()
    return HttpResponseRedirect(reverse('viewEvents'))
