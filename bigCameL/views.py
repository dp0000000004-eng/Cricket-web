from rest_framework.response import Response
from .models import Teams, Players, Matches, Venues, TotalSit, Champs, SitPrice, FanOfIPL, IPLMeta, City, Blog
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.decorators import api_view

@api_view()
def blog_view(request):

    blogs = Blog.objects.all()

    blogs_obj = [model_to_dict(blog)for blog in blogs]

    return Response(blogs_obj, status=status.HTTP_200_OK)


@api_view()
def city_view(request):
    cities = City.objects.all()

    cities_obj = [model_to_dict(city)for city in cities]

    return Response(cities_obj, status=status.HTTP_200_OK)

@api_view()
def team_view(request):

    teams = Teams.objects.all()

    teams_obj = [model_to_dict(team)for team in teams]

    return Response(teams_obj, status=status.HTTP_200_OK)


@api_view()
def player_view(request, team_id):

    players = Players.objects.filter(team=team_id)

    players_obj = [model_to_dict(player)for player in players]

    return Response(players_obj, status=status.HTTP_200_OK)


@api_view()
def home(request):

    ipl = IPLMeta.objects.all()

    ipl_obj = [model_to_dict(pl)for pl in ipl]

    return Response(ipl_obj, status=status.HTTP_200_OK)

@api_view()
def matches_view(request):

    matches = Matches.objects.all()

    matches_obj = [model_to_dict(match)for match in matches]

    return Response(matches_obj, status=status.HTTP_200_OK)


def venue_view(request):
    venues = Venues.objects.all()

    venues_obj = [model_to_dict(venue)for venue in venues]



#   ERROR IN THIS FUNCTION
@api_view()
def booking(request):
    

    sit_left = TotalSit.objects.first().sit_available
    vip_sit_price = SitPrice.objects.all()[0].price
    normal_sit_price = SitPrice.objects.all()[1].pricern 
    

    sit_available = TotalSit.objects.all()

    context = {
        [model_to_dict(sit_left)],
        [model_to_dict(vip_sit_price)],
        [model_to_dict(normal_sit_price)],

    }

    return Response(context, status=status.HTTP_200_OK)


@api_view()
def champs(request):
    champs = Champs.objects.all()

    champs_obj = [model_to_dict(champ) for champ in champs]

    return Response(champs_obj, status=status.HTTP_200_OK)


@api_view()
def fam_view(request):


    fams = FanOfIPL.objects.all()

    fams_obj = [model_to_dict(fam)for fam in fams]

    return Response(fams_obj, status=status.HTTP_200_OK)
