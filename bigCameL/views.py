from django.shortcuts import render, redirect
from .models import Teams, Players, Matches, Venues, About_venue, TotalSit
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import BookingForm
from django.contrib.auth.decorators import login_required


# Create your views here.



def team_view(request):
    teams = Teams.objects.all()
    return render(request, "pl/teams.html", {"teams":teams})


def player_view(request, team_id):
    players = Players.objects.filter(team=team_id)
    return render(request, "pl/players.html", {"players":players})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, message="Invalid Username or password!")

    return render(request, "pl/login.html")


@login_required
def home(request):
    return render(request, "pl/home.html")

def about_venue(request, venue_id):
    about_venues = About_venue.objects.filter(id=venue_id)
    return render(request, "pl/about_venue.html", {"about_venues":about_venues})

def matches_view(request):
    matches = Matches.objects.all()
    return render(request, "pl/matches.html", {"matches":matches})

def venue_view(request):
    venues = Venues.objects.all()
    return render(request, "pl/venues.html", {"venues":venues})

def booking(request):
    sit_available = TotalSit.objects.all()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = BookingForm()

    return render(request, "pl/book.html" , {"form":BookingForm(request.POST), "total_available":sit_available})