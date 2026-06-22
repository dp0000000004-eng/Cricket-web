from django.urls import path
from . import views


urlpatterns = [
    path("", views.login_view, name="login"),
    path("home/", views.home, name="home"),
    path("teams/", views.team_view, name="team_view"),
    path("players/<int:team_id>/", views.player_view, name="player_view"),
    path("matches/", views.matches_view, name="match_view"),
    path("venues/", views.venue_view, name="venue_view"),
    path("about_venue/<int:venue_id>/", views.about_venue, name="about_venue"),
    path("book/<int:user_id>/", views.booking, name="book"),
    path("create_a_c/", views.createAccount, name="createAccount"),
]