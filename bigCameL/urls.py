
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("city/", views.city_view, name="city"),
    path("teams/", views.team_view, name="team_view"),
    path("players/<int:team_id>/", views.player_view, name="player_view"),
    path("matches/", views.matches_view, name="match_view"),
    path("venues/", views.venue_view, name="venue_view"),
    path("book/", views.booking, name="book"),
    path("champs/", views.champs, name="blog"),
    path("fam/", views.fam_view, name="fam"),
    path("blog/", views.blog_view, name="blog"),
]