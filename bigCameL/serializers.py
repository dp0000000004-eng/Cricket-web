from .models import City, Teams, Video, IPLMeta
from rest_framework import serializers
from .models import Official_code_of_playertype
from .models import Venues, Players, Matches
from .models import About_venue, Blog, Champs
from .models import FanOfIPL
import bleach


def sanitize_value(value):
    if isinstance(value, str):
        return bleach.clean(value)
    return value


class CitySerializer(serializers.ModelSerializer):
    def validate_city(self, value):
        return sanitize_value(value)
    def validate_code(self, value):
        return sanitize_value(value)
    class Meta:
        model = City
        fields = ['id', 'city', 'code']


class TeamsSerializer(serializers.ModelSerializer):
    def validate_team_name(self, value):
        return sanitize_value(value)
    def validate_code(self, value):
        return sanitize_value(value)
    class Meta:
        model = Teams
        fields = ['id', 'team_name', 'code']


class VideoSerializers(serializers.ModelSerializer):
    def validate_title(self, value):
        return sanitize_value(value)
    def validate_video_url(self, value):
        return sanitize_value(value)
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_url']


class MetaSerializer(serializers.ModelSerializer):
    def validate_total_team(self, value):
        return sanitize_value(value)
    def validate_total_matches(self, value):
        return sanitize_value(value)
    def validate_total_venue(self, value):
        return sanitize_value(value)
    class Meta:
        model = IPLMeta
        fields = ['id', 'total_team', 'total_matches', 'total_venue']


class Official_code_of_playertypeSerializer(serializers.ModelSerializer):
    def validate__type(self, value):
        return sanitize_value(value)
    def validate_code(self, value):
        return sanitize_value(value)
    class Meta:
        model = Official_code_of_playertype
        fields = ['id', '_type', 'code']


class VenuesSerializer(serializers.ModelSerializer):
    def validate_venue_name(self, value):
        return sanitize_value(value)
    def validate_code(self, value):
        return sanitize_value(value)
    def validate_city(self, value):
        return sanitize_value(value)
    def validate_home_ground_of(self, value):
        return sanitize_value(value)
    
    class Meta:
        model = Venues
        fields = ['id', 'venue_name', 'code', 'city', 'home_ground_of']


class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()
    code = serializers.StringRelatedField()

    def validate_player_name(self, value):
        return sanitize_value(value)
    def validate_jersey_no(self, value):
        return sanitize_value(value)
    def validate_is_overseas(self, value):
        return sanitize_value(value)
    def validate_is_captain(self, value):
        return sanitize_value(value)
    def validate_team(self, value):
        return sanitize_value(value)
    def validate_code(self, value):
        return sanitize_value(value)
    class Meta:
        model = Players
        fields = ['id', 'player_name', 'jersey_no', 'is_overseas', 'is_captain', 'team', 'code']


class AboutVenueSerializer(serializers.ModelSerializer):
    venue_name = serializers.StringRelatedField()

    def validate_venue_name(self, value):
        return sanitize_value(value)
    def validate_vanue_people_capa(self, value):
        return sanitize_value(value)
    def validate_venue_width(self, value):
        return sanitize_value(value)
    def validate_description(self, value):
        return sanitize_value(value)
    class Meta:
        model = About_venue
        fields = ['id', 'venue_name', 'venue_people_capa', 'venue_width', 'description']


class ChampsSerializer(serializers.ModelSerializer):
    def validate_year(self, value):
        return sanitize_value(value)
    def validate_champs(self, value):
        return sanitize_value(value)

    class Meta:
        model = Champs
        fields = ['id', 'year', 'champs']


class BlogSerializer(serializers.ModelSerializer):
    year = serializers.StringRelatedField()

    def validate_year(self, value):
        return sanitize_value(value)
    def validate_Blog(self, value):
        return sanitize_value(value)
    
    class Meta:
        model = Blog
        fields = ['id', 'year', 'Blog']


class MatchesSerializer(serializers.ModelSerializer):
    team1 = serializers.StringRelatedField()
    team2 = serializers.StringRelatedField()
    venues = serializers.StringRelatedField()
    home_of = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    def validate_team1(self, value):
        return sanitize_value(value)
    def validate_team2(self, value):
        return sanitize_value(value)
    def validate_venues(self, value):
        return sanitize_value(value)
    def validate_home_of(self, value):
        return sanitize_value(value)
    def validate_date_time(self, value):
        return sanitize_value(value)
    def validate_city(self, value):
        return sanitize_value(value)
    class Meta:
        model = Matches
        fields = ['id', 'team1', 'team2', 'venues', 'home_of', 'date_time', 'city']


class FamSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField()

    def validate_username(self, value):
        return sanitize_value(value)
    def validate_email(self, value):
        return sanitize_value(value)
    def validate_title(self, value):
        return sanitize_value(value)
    def validate_fan_image(self, value):
        return sanitize_value(value)
    def validate_descriptions(self, value):
        return sanitize_value(value)
    class Meta:
        model = FanOfIPL
        fields = ['id', 'username', 'email', 'title', 'fan_image', 'descriptions']