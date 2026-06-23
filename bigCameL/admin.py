from django.contrib import admin
from .models import City, Teams, Official_code_of_playertype, Venues, Players, Matches, About_venue, SitType, TotalSit, SitPrice, TotalBooked, Video

# Register your models here.


admin.site.register(City)
admin.site.register(Teams)
admin.site.register(Official_code_of_playertype)
admin.site.register(Venues)
admin.site.register(Players)
admin.site.register(Matches)
admin.site.register(About_venue)
admin.site.register(SitType)
admin.site.register(TotalSit)
admin.site.register(SitPrice)
admin.site.register(TotalBooked)
admin.site.register(Video)