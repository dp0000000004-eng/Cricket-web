from django.shortcuts import render, redirect
from .models import Teams, Players, Matches
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
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


def matches_view(request):
    matches = Matches.objects.all()
    return render(request, "pl/matches.html", {"matches":matches})