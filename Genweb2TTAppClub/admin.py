from django.contrib import admin
from .models import Match, Team, Player

# Register your models here.
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Player)