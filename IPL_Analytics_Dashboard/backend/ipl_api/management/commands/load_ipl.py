# ipl_api/management/commands/load_ipl.py
import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from ipl_api.models import Match, Delivery
import os

# DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'data')


class Command(BaseCommand):
    help = 'Load IPL matches and deliveries CSV into DB'

    def handle(self, *args, **options):
        matches_file = os.path.join(DATA_DIR, 'matches.csv')
        deliveries_file = os.path.join(DATA_DIR, 'deliveries.csv')

        self.stdout.write("Loading matches...")
        with open(matches_file, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            matches = []
            for row in reader:
                try:
                    mid = int(row.get('id') or row.get('match_id') or row.get('matchId'))
                except:
                    continue
                m = Match(
                    id=mid,
                    season=int(row.get('season') or 0),
                    city=row.get('city') or '',
                    date=row.get('date') or None,
                    team1=row.get('team1') or '',
                    team2=row.get('team2') or '',
                    toss_winner=row.get('toss_winner') or '',
                    toss_decision=row.get('toss_decision') or '',
                    result=row.get('result') or '',
                    dl_applied=int(row.get('dl_applied') or 0),
                    winner=row.get('winner') or '',
                    win_by_runs=int(row.get('win_by_runs') or 0),
                    win_by_wickets=int(row.get('win_by_wickets') or 0),
                    player_of_match=row.get('player_of_match') or '',
                    venue=row.get('venue') or '',
                )
                matches.append(m)
            Match.objects.all().delete()
            Match.objects.bulk_create(matches, batch_size=5000)
        self.stdout.write(self.style.SUCCESS("Matches loaded"))

        self.stdout.write("Loading deliveries...")
        with open(deliveries_file, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            Delivery.objects.all().delete()
            deliveries = []
            for row in reader:
                # Some datasets call it match_id or id: try both
                match_id = int(row.get('match_id') or row.get('id') or row.get('matchId'))
                d = Delivery(
                    match_id=match_id,
                    inning=int(row.get('inning') or 0),
                    batting_team=row.get('batting_team') or row.get('battingTeam') or '',
                    bowling_team=row.get('bowling_team') or row.get('bowlingTeam') or '',
                    over=int(row.get('over') or 0),
                    ball=int(row.get('ball') or 0),
                    batsman=row.get('batsman') or '',
                    bowler=row.get('bowler') or '',
                    is_super_over=int(row.get('is_super_over') or 0),
                    wide_runs=int(row.get('wide_runs') or 0),
                    bye_runs=int(row.get('bye_runs') or 0),
                    legbye_runs=int(row.get('legbye_runs') or 0),
                    noball_runs=int(row.get('noball_runs') or 0),
                    penalty_runs=int(row.get('penalty_runs') or 0),
                    batsman_runs=int(row.get('batsman_runs') or 0),
                    extra_runs=int(row.get('extra_runs') or 0),
                    total_runs=int(row.get('total_runs') or 0),
                    player_dismissed=row.get('player_dismissed') or '',
                    dismissal_kind=row.get('dismissal_kind') or '',
                    fielder=row.get('fielder') or ''
                )
                deliveries.append(d)
                if len(deliveries) >= 5000:
                    Delivery.objects.bulk_create(deliveries, batch_size=5000)
                    deliveries = []
            if deliveries:
                Delivery.objects.bulk_create(deliveries, batch_size=5000)
        self.stdout.write(self.style.SUCCESS("Deliveries loaded"))
