from django.shortcuts import render, redirect
from .models import Teams, Players, Matches, Venues, About_venue, TotalSit, Video, Champs, Blog, SitPrice
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import BookingForm, UserForm, FamForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random


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
            return redirect('book')
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


def booking(request):
    if request.user.is_authenticated:



        greetMsg = [
                    "welcome ",
                    "Have a Good day ",
                    "hello, ",
                    "nice coffe, "
                ]
        

        sit_left = TotalSit.objects.first().sit_available
        vip_sit_price = SitPrice.objects.all()[0].price
        normal_sit_price = SitPrice.objects.all()[1].price
        nothing_left = 0

        if sit_left == nothing_left:
            info_msg = messages.info(request, message="No sit available")
            return render(request, "pl/book.html" , {"info_msg":info_msg})


        sit_available = TotalSit.objects.all()

        if sit_left != nothing_left:
            if request.method == "POST":



                form = BookingForm(request.POST)
                if form.is_valid():
                    book = form.save(commit=False)
                    book.username = request.user
                    book.save()
                    messages.success(request, message="Thank's For Booking")
                    form = BookingForm()
                else:
                    form = BookingForm()

        return render(request, "pl/book.html" , {"form":BookingForm(request.POST), "total_available":sit_available, "vip_price":vip_sit_price, "normal_price":normal_sit_price, "greet":random.choice(greetMsg)})
    else:
        return redirect("login")


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
    last_count = Champs.objects.count()
    if team_id > last_count:
        return redirect('blog')
    if team_id <= last_count:
        blog = Blog.objects.filter(year=team_id)
        if team_id == 0:
            return redirect('blog')
        
        return render(request, "pl/blog.html", {"blog":blog, "team_id":team_id, "last_count":last_count})


def fam_view(request, user_id):
    

    greetings = [
        "Thanks for the love, have a nice day!",
        "Wishing you joy and sunshine all day long!",
        "Stay positive, stay happy, stay blessed!",
        "Good vibes only — keep smiling!",
        "May your day be filled with peace and laughter!",
        "Sending warm wishes your way!",
        "Happiness looks good on you — enjoy your day!",
        "Gratitude makes the day brighter!",
        "Cheers to a wonderful day ahead!",
        "Keep shining, the world needs your light!"
    ]


    if request.method == 'POST':
        form = FamForm(request.POST, request.FILES)
        if form.is_valid():
            fam = form.save(commit=False)
            fam.name = request.user
            fam.save()
            messages.success(request, message="thanks for Love, Have Nice Day!")