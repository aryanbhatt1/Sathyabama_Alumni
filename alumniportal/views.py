from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import *
from .forms import AlumniSignUpForm


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
            print(username)
            print(first_name)
            return redirect('home')
    else:
        form = AlumniSignUpForm()
    return render(request, 'pages/auth/signup.html', {'form': form})


@login_required
def Dashboard(request):
    return render(request, 'pages/admin/dashboard.html', context={})


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
