from .models import City, Teams, Video, IPLMeta
from rest_framework import serializers
from .models import Official_code_of_playertype
from .models import Venues, Players, Matches
from .models import About_venue



class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city', 'code']


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ['id', 'team_name', 'code']


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_url']


class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPLMeta
        fields = ['id', 'total_team', 'total_matches', 'total_venue']


class Official_code_of_playertypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Official_code_of_playertype
        fields = ['id', '_type', 'code']


class About_venueSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_venue
        fields = ['id', 'venue_name', 'venue_people_capa', 'venue_width', 'description']


class VenuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venues
        fields = ['id', 'venue_name', 'code', 'city', 'home_ground_of']

class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()
    code = serializers.StringRelatedField()
    class Meta:
        model = Players
        fields = ['id', 'player_name', 'jersey_no', 'is_overseas' , 'is_captain', 'team', 'code']