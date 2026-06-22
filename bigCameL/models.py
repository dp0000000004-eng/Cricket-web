from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class City(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.city} {self.code}"


class Teams(models.Model):
    team_name = models.CharField(max_length=64)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.team_name} {self.code}"
    
class Official_code_of_playertype(models.Model):
    _type = models.CharField(max_length=24)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self._type} {self.code}"
    
class Venues(models.Model):
    venue_name = models.CharField(max_length=64)
    code = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="venue_in_city")
    home_ground_of = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="home_team", blank=True)

    def __str__(self):
        return f"{self.venue_name} {self.code}, {self.home_ground_of} {self.city}"
    
class Players(models.Model):
    player_name = models.CharField(max_length=64)
    jersey_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
    is_overseas = models.BooleanField(default=False)
    is_captain = models.BooleanField(default=False)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="team_player", blank=True)
    code = models.ForeignKey(Official_code_of_playertype, on_delete=models.CASCADE, related_name="type_code")

    def __str__(self):
        return f"{self.player_name} {self.team} {self.code} {self.jersey_no}"
    

class Matches(models.Model):
    team1 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="match_team_1")
    team2 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="match_team_2")
    venue = models.ForeignKey(Venues, on_delete=models.CASCADE, related_name="match_venue")
    home_of = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="home_tema_match")
    date_time = models.DateTimeField(blank=True ,null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="match_city")


    def __str__(self):
        return f"{self.team1} {self.team2} {self.venue} {self.home_of} {self.city} {self.city}"
    

class About_venue(models.Model):
    venue_name = models.ForeignKey(Venues, on_delete=models.CASCADE, related_name="stadium_name")
    venue_people_capa = models.IntegerField()
    venue_width = models.IntegerField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.venue_people_capa} {self.venue_width} {self.description} "
    
class SitType(models.Model):
    sit_type = models.CharField(max_length=24)

    def __str__(self):
        return f"{self.sit_type} "
    
class SitPrice(models.Model):
    sit_type = models.ForeignKey(SitType, on_delete=models.CASCADE, related_name="price_sit")
    price = models.FloatField()

    def __str__(self):
        return f"{self.sit_type} {self.price}"

class TotalSit(models.Model):
    sit_available = models.IntegerField()
    vip = models.IntegerField()
    normal = models.IntegerField()

    def save(self, *args, **kwargs):
        self.sit_available = self.vip + self.normal
        super().save(*args, **kwargs)

    def __str__(self):
        return f" {self.sit_available} {self.vip} {self.normal}"
    
class TotalBooked(models.Model):
    sit = models.ForeignKey(TotalSit, on_delete=models.CASCADE, related_name="sit_book", default=TotalSit.objects.first)
    total_booked = models.IntegerField(blank=True, null=True)
    vip = models.IntegerField(blank=True, null=True)
    normal = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_booked = (self.vip or 0) + (self.normal or 0)
        super().save(*args, **kwargs)

        if self.sit:
            self.sit.vip -= (self.vip or 0)
            self.sit.normal -= (self.normal or 0)

            self.sit.vip = max(self.sit.vip, 0)
            self.sit.normal = max(self.sit.normal, 0)
            self.sit.sit_available = self.sit.vip + self.sit.normal
            self.sit.save()



    def __str__(self):
        return f"{self.total_booked} {self.vip} {self.normal}"