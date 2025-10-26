# ipl_api/models.py
from django.db import models

class Match(models.Model):
    id = models.IntegerField(primary_key=True)   # matches.csv id
    season = models.IntegerField()
    city = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    team1 = models.CharField(max_length=100, null=True, blank=True)
    team2 = models.CharField(max_length=100, null=True, blank=True)
    toss_winner = models.CharField(max_length=100, null=True, blank=True)
    toss_decision = models.CharField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=50, null=True, blank=True)
    dl_applied = models.IntegerField(null=True, blank=True)
    winner = models.CharField(max_length=100, null=True, blank=True)
    win_by_runs = models.IntegerField(null=True, blank=True)
    win_by_wickets = models.IntegerField(null=True, blank=True)
    player_of_match = models.CharField(max_length=255, null=True, blank=True)
    venue = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.season} - {self.team1} vs {self.team2}"

class Delivery(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='deliveries')
    inning = models.IntegerField(null=True)
    batting_team = models.CharField(max_length=100)
    bowling_team = models.CharField(max_length=100)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=150, null=True)
    bowler = models.CharField(max_length=150, null=True)
    is_super_over = models.IntegerField(null=True, blank=True)
    wide_runs = models.IntegerField(default=0)
    bye_runs = models.IntegerField(default=0)
    legbye_runs = models.IntegerField(default=0)
    noball_runs = models.IntegerField(default=0)
    penalty_runs = models.IntegerField(default=0)
    batsman_runs = models.IntegerField(default=0)
    extra_runs = models.IntegerField(default=0)
    total_runs = models.IntegerField(default=0)
    player_dismissed = models.CharField(max_length=150, null=True, blank=True)
    dismissal_kind = models.CharField(max_length=50, null=True, blank=True)
    fielder = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['bowling_team']),
            models.Index(fields=['bowler']),
            models.Index(fields=['match']),
        ]
