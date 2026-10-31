import os
import requests
import random
import requests
import logging
from django.views import View
from django.shortcuts import render, redirect
from .models import Teams, Players, Matches, Venues, About_venue, TotalSit, Video
from .models import Champs, Blog, SitPrice, FanOfIPL, IPLMeta
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import BookingForm, UserForm, FamForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from dotenv import load_dotenv
from .serializers import TeamsSerializer, VideoSerializers, MetaSerializer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.response import Response
from .serializers import VenuesSerializer, PlayerSerializer, AboutVenueSerializer
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_csv.renderers import CSVRenderer
from .serializers import ChampsSerializer, BlogSerializer, MatchesSerializer
from .serializers import FamSerializer, TotalSitSerializer
from django.http import HttpResponse
from requests import RequestException
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.decorators import throttle_classes, permission_classes
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator, EmptyPage
from .throttles import MatchesThrottle
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
from django.template.loader import render_to_string


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, XMLRenderer, CSVRenderer])
def team_view(request):
    teams = Teams.objects.all()
    teams_serializer = TeamsSerializer(teams, many=True)
    return Response(
        {
            'teams':teams_serializer.data
        },
        template_name='pl/teams.html'
    )


@api_view(['POST', 'GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, XMLRenderer, YAMLRenderer, CSVRenderer])
def player_view(request, team_id):
    players = Players.objects.filter(team=team_id).select_related('team', 'code').all()
    playersSerializer = PlayerSerializer(players, many=True)
    return Response({'players':playersSerializer.data} ,template_name="pl/players.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        back_path = f"{request.POST.get('next') or request.GET.get('next') or 'home'}"

        if user is not None:
            login(request, user)
            return redirect(back_path)
        else:
            messages.error(request, message="Invalid Username or password!")

    return render(request, "pl/login.html")

logger = logging.getLogger(__name__)

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, XMLRenderer, YAMLRenderer])
@throttle_classes([AnonRateThrottle])
def home(request):

    

    load_dotenv()

    try:

        api_key = os.getenv('openwether_api_key')

        lat = float(os.getenv('lat'))
        lon = float(os.getenv('lon'))
        Temp = None
        Weather = None
        Wind_speed = None

    
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}"
        response = requests.get(url)
        data = response.json()


        Temp = data['list'][0]['main']['temp']
        Weather = data['list'][0]['weather'][0]['description']
        Wind_speed = data['list'][0]['wind']['speed']

        

        ipl = IPLMeta.objects.all()
        videos = Video.objects.all()
        metaSerializer = MetaSerializer(ipl, many=False)
        videosSerializer = VideoSerializers(videos, many=True)


        return Response(

            {
                # 'data':data,
                "videos":videosSerializer.data, 
                "ipl":metaSerializer.data,
                "temp":Temp,
                "wethr_desc":Weather,
                "wind":Wind_speed
            },

            template_name='pl/home.html'
        )

    except Exception as e:
        logger.error(f"The Error is: {type(e).__name__} : {e}")


        ipl = IPLMeta.objects.all()
        videos = Video.objects.all()
        metaSerializer = MetaSerializer(ipl, many=True)
        videosSerializer = VideoSerializers(videos, many=True)

    


        return Response(

            {
                # 'data':data,
                "videos":videosSerializer.data, 
                "ipl":metaSerializer.data,
                "temp":None,
                "wethr_desc": None,
                "wind":None,
                "error":str(type(e).__name__)
            },

            template_name='pl/home.html'
        )


"""
This class Based view is for experiment purpose 
For production server Use function baserd view insted
"""
class Home(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    

    template_name = "pl/home.html"


    def get(self, request):
        return Response(template_name=self.template_name)




@api_view(['POST', 'GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, XMLRenderer, CSVRenderer])
@permission_classes([IsAuthenticated])
def about_venue(request, venue_id):
    about_venues = About_venue.objects.filter(id=venue_id).select_related('stadium_name')
    about_venueSerializer = AboutVenueSerializer(about_venues, many=True)
    
    return Response(
        {
            'about_venues':about_venueSerializer.data,
        }
        ,
        template_name='pl/about_venue.html'
    )




@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, XMLRenderer, CSVRenderer])
@permission_classes([IsAuthenticated])
@throttle_classes([MatchesThrottle])
def matches_view(request):
    matches = Matches.objects.all().select_related('team1', 'team2' , 'venue', 'home_of', 'city')
    matchesSerializer = MatchesSerializer(matches, many=True)
    return Response({"matches":matchesSerializer.data}, template_name="pl/matches.html")






@api_view([ 'GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, XMLRenderer])
def venue_view(request):
    venues = Venues.objects.all()
    venuesSerializer = VenuesSerializer(venues, many=True)
    return Response(
        
        {
            "venues":venuesSerializer.data
        },

        template_name="pl/venues.html"
    )


def booking(request):
    if request.user.is_authenticated:

        c_username = request.user.username
        email = request.user.email

        user_data = {
            "username":c_username,
            "email":email
        }

        greetMsg = [
            "welcome ",
            "Have a Good day ",
            "Hello, ",
            "nice coffee, "
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
                    book.user_data = user_data
                    book.save()
                    messages.success(request, message="Thank's For Booking")
                    form = BookingForm()
                else:
                    form = BookingForm()

        return render(request, "pl/book.html" , {
            "form":BookingForm(request.POST), 
            "total_available":sit_available,
            "vip_price":vip_sit_price, 
            "normal_price":normal_sit_price, 
            "greet":random.choice(greetMsg), 
            "user_data":request.user.username
        })
    else:
        return redirect("login")


def createAccount(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        raw_password = request.POST.get("password")

        request.session['otp_data'] = {
            'username':username,
            'password':raw_password,
            'email':email
        }

        return redirect('otp')


    return render(request, "pl/create_a_c.html")

logger = logging.getLogger(__name__)

def email_validator(request, expiry_minutes=10, otp=random.randint(int(os.getenv('otp_min_range')), int(os.getenv('otp_max_range')))):

    load_dotenv()
    email_sent = False

    data = request.session.get('otp_data')

    if not data:
        return redirect('createAccount')

    username = data['username']
    password = data['password']
    email = data['email']


    app_name = "CrickWat"
    logger.error(otp)

    

    html = render_to_string("email.html", {
        "otp": otp,
        "user_name": username,
        "app_name": app_name,
        "expiry_minutes": expiry_minutes,
    })
    text = f"Hi {username}, your {app_name} verification code is {otp}. It expires in {expiry_minutes} minutes."

    try:
        response = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={
                "api-key": os.getenv('brevo_api_key'),
                "Content-Type": "application/json",
            },
            json={
                "sender": {"name": "PawBytes Team", "email": os.getenv('brevo_user')},
                "to": [{"email": email, "name": username}],
                "subject": f"{otp} is your {app_name} verification code",
                "htmlContent": html,
                "textContent": text,
            },
            timeout=5,
        )


        response.raise_for_status()

        if request.method == "POST":
            logger.error(otp)

            user_otp = request.POST.get('otp')
            if int(user_otp) == otp:
                user = User(
                    username=username,
                    email=email
                )
                user.set_password(password)
                user.save()
                del request.session['otp_data']
                messages.success(request, message="OTP verifyed successfully")
                return redirect('home')
            else:
                messages.error(request, message="Invaild OTP !")


        return render(request, "pl/email_otp.html", {"email_sent":email_sent})
    except Exception as e:
        logger.error(f"The error is: {type(e).__name__}: {e}")
        return render(request, "pl/email_otp.html")



def logout_view(request):
    logout(request)
    return redirect("home")



@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, XMLRenderer, YAMLRenderer, CSVRenderer])
def champs(request):
    champs = Champs.objects.all()
    champsSerializer = ChampsSerializer(champs, many=True)
    return Response({"champs":champsSerializer.data}, template_name="pl/champs.html")


@api_view([ 'GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, XMLRenderer, YAMLRenderer, CSVRenderer])
def blog_view(request, team_id):
    champs_ = Champs.objects.all().count()
    champs_count = []

    for c in range(champs_):
        champs_count.append(c+1)

    
    last_count = Champs.objects.count()

    if team_id > last_count:
        return redirect('blog')
    if team_id <= last_count:
        blog = Blog.objects.get(pk=team_id)
        blogSerializer = BlogSerializer(blog, many=False)
        if team_id == 0:
            return redirect('blog')
        
        return Response(
            {
            "blog":blogSerializer.data, 
            "team_id":team_id, 
            "last_count":last_count, 
            "champs_count":champs_count
            },
            template_name='pl/blog.html'
        )



@api_view(['GET','POST'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, XMLRenderer, YAMLRenderer, CSVRenderer])
def fam_view(request):
    is_ajax = request.headers.get("x-requested-with") == "XMLHttpRequest"

    if request.user.is_authenticated:

        fams = FanOfIPL.objects.all()

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
                fam.username = request.user
                fam.save()
                if is_ajax:
                    return JsonResponse({"message": "Upload successful."})
                messages.success(request, "Done  ")
                return redirect("fam")
            if is_ajax:
                return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
        else:
            form = FamForm()


        perpage = request.query_params.get('perpage', default=3)
        page = request.query_params.get('page', default=1)


        fams = FanOfIPL.objects.all()
        paginator = Paginator( fams, per_page=perpage)

        try:
            fams = paginator.page(number=page)
        except EmptyPage:
            fams = []
        
        famSerializer = FamSerializer(fams, many=True)
        if request.accepted_renderer.format == "html":
            
            return Response(
                    {
                        "form":form, 
                        "greetings":random.choice(greetings), 
                        "fams":famSerializer.data
                    }, 
                    template_name="pl/fam.html")
        
        else:
            return Response({
                
                    "greetings":random.choice(greetings), 
                    "fams":famSerializer.data
                },

                template_name="pl/fam.html"
            )
    else:
        if request.method == 'GET' and is_ajax:
            # return JsonResponse({"error": "You must be logged in to upload."}, status=403)

            perpage = request.query_params.get('perpage', default=3)
            page = request.query_params.get('page', default=1)


            fams = FanOfIPL.objects.all()
            paginator = Paginator( fams, per_page=perpage)

            try:
                fams = paginator.page(number=page)
            except EmptyPage:
                fams = []
            
            famSerializer = FamSerializer(fams, many=True)
            return Response(
                {
                    'fams':famSerializer.data
                },
                template_name="pl/fam.html"
            )
    data = {"greetings": random.choice(greetings), "fams": famSerializer.data}

    

def delete_fan_data(request, fan_id):
    fan = FanOfIPL.objects.get(id=fan_id)

    fan.delete()
    fan.fan_image.delete(save=False)
    return redirect("fam")



@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def totalSitAPIView(request):
    items = TotalSit.objects.all()[0]

    sitSerializer = TotalSitSerializer(items)

    store_data = TotalSitSerializer(data=request.data)
    store_data.is_valid(raise_exception=True)
    store_data.save()

    return Response(
        {"items":sitSerializer.data}
    )


def getJWTToken(request):
    return render(request, 'pl/jwtToken.html')


def refreshJWTToken(request):
    return render(request, 'pl/jwtRefresh.html')
    


@permission_classes([HasAPIKey])

def generateAPIkey(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            api_key, key = APIKey.objects.create_key(name="my-remote-service")


            return render(request, 'pl/APIKey.html', {"key":key, "prefix":api_key.prefix})

        else:
            return render(request, 'pl/APIKey.html', {"error":"Invalid Credentials !"})


    return render(request, 'pl/APIKey.html')


def check(request):
    return HttpResponse({("Hello, World")})