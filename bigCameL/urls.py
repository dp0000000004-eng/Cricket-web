
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import Home

urlpatterns = [

    path("login/", views.login_view, name="login"),
    path("", views.Home.as_view(), name="home"),
    path("teams/", views.team_view, name="team_view"),
    path("players/<int:team_id>/", views.player_view, name="player_view"),
    path("matches/", views.matches_view, name="match_view"),
    path("venues/", views.venue_view, name="venue_view"),
    path("about_venue/<int:venue_id>/", views.about_venue, name="about_venue"),
    path("book/", views.booking, name="book"),
    path("create_a_c/", views.createAccount, name="createAccount"),
    path("logout/", views.logout_view, name="logout"),
    path("champs/", views.champs, name="blog"),
    path("blog/<int:team_id>/", views.blog_view, name="full_blog"),
    path("fam/", views.fam_view, name="fam"),
    path("delete/<int:fan_id>", views.delete_fan_data, name="delete_fam"),
    path('sit-data/', views.totalSitAPIView, name="sit_data"),
    path('token-html/', views.getJWTToken, name="jwt_html"),
    path('token/', TokenObtainPairView.as_view(), name="token_obtainpair"),
    path('token/refresh/', TokenRefreshView.as_view() , name="token_pair_refresh"),
    path('token-refresh-html/', views.refreshJWTToken, name="refresh_tokne_html"),
    path('api/', views.generateAPIkey, name="get_api"),
    path('email-verify/', views.email_validator, name="otp"),
    path('hello/', views.check, name="check"),
    
]
