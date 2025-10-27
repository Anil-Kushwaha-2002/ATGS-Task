# ipl_api/models.py
from django.db import models

class Match(models.Model):
    match_id = models.IntegerField(primary_key=True)
    season = models.IntegerField()
    city = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    toss_winner = models.CharField(max_length=100, null=True, blank=True)
    toss_decision = models.CharField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=50, null=True, blank=True)
    dl_applied = models.IntegerField(null=True, blank=True)
    winner = models.CharField(max_length=100, null=True, blank=True)
    win_by_runs = models.IntegerField(null=True, blank=True)
    win_by_wickets = models.IntegerField(null=True, blank=True)
    venue = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.match_id} - {self.season}"

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="deliveries")
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=100)
    bowling_team = models.CharField(max_length=100)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=100)
    bowler = models.CharField(max_length=100)
    is_super_over = models.IntegerField(null=True, blank=True)
    wide_runs = models.IntegerField(null=True, blank=True)
    bye_runs = models.IntegerField(null=True, blank=True)
    legbye_runs = models.IntegerField(null=True, blank=True)
    noball_runs = models.IntegerField(null=True, blank=True)
    penalty_runs = models.IntegerField(null=True, blank=True)
    batsman_runs = models.IntegerField(null=True, blank=True)
    extra_runs = models.IntegerField(null=True, blank=True)
    total_runs = models.IntegerField(null=True, blank=True)
    player_dismissed = models.CharField(max_length=100, null=True, blank=True)
    dismissal_kind = models.CharField(max_length=50, null=True, blank=True)
    fielder = models.CharField(max_length=100, null=True, blank=True)
