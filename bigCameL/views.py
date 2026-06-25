from django.shortcuts import render, redirect
from .models import Teams, Players, Matches, Venues, About_venue, TotalSit, Video, Champs, Blog
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import BookingForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.



def team_view(request):
    teams = Teams.objects.all()
    return render(request, "pl/teams.html", {"teams":teams})


def player_view(request, team_id):
    players = Players.objects.filter(team=team_id)
    return render(request, "pl/players.html", {"players":players})

def login_view(request):
    if request.user.is_authenticated:
        redirect('home')
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



def home(request):
    videos = Video.objects.first()
    return render(request, "pl/home.html", {"videos":videos})

def about_venue(request, venue_id):
    about_venues = About_venue.objects.filter(id=venue_id)
    return render(request, "pl/about_venue.html", {"about_venues":about_venues})

def matches_view(request):
    matches = Matches.objects.all()
    return render(request, "pl/matches.html", {"matches":matches})

def venue_view(request):
    venues = Venues.objects.all()
    return render(request, "pl/venues.html", {"venues":venues})

@login_required
def booking(request, user_id):
    sit_available = TotalSit.objects.all()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.username = request.user
            book.save()
            messages.success(request, message="Thank's For Booking")
        else:
            form = BookingForm()

    return render(request, "pl/book.html" , {"form":BookingForm(request.POST), "total_available":sit_available})


def createAccount(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        raw_password = request.POST.get("password")
        user = User(username=username, email=email)
        user.set_password(raw_password)
        user.save()
        messages.success(request, message="Account Created")
    return render(request, "pl/create_a_c.html", {"form":UserForm(request.POST)})

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


def champs(request):
    champs = Champs.objects.all()
    return render(request, "pl/champs.html" ,{"champs":champs})

def blog_view(request, team_id):
    blog = Blog.objects.filter(year=team_id)
    return render(request, "pl/blog.html", {"blog":blog})