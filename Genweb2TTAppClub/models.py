from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Player(models.Model):
    PlayerID = models.AutoField(primary_key=True)
    PlayerName = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'player'

    def __str__(self):
        return self.PlayerName


class Team(models.Model):
    TeamID = models.AutoField(primary_key=True)
    TeamName = models.CharField(max_length=200)
    PlayerOneID = models.ForeignKey(Player, on_delete=models.CASCADE,)
    PlayerTwoID = models.ForeignKey(Player, related_name="player_two",on_delete=models.CASCADE, null=True)
    #Match = models.ForeignKey(Match, db_column="MatchID", on_delete=models.CASCADE)
    Score = models.IntegerField(default= 0, null=True)

    class Meta:
        managed = True
        db_table = 'team'

    def __str__(self):
        return self.TeamName

class Match(models.Model):
    MatchID = models.AutoField(primary_key=True)
    MatchName = models.CharField(max_length=200)
    MatchDate = models.DateField(auto_now=False, auto_now_add=False)
    MatchType = models.CharField(max_length=200, null=True)

    TeamOneID = models.ForeignKey(Team, on_delete=models.CASCADE)
    TeamTwoID = models.ForeignKey(Team, related_name="team_two_match", on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'match'

    def __str__(self):
        return self.MatchName
