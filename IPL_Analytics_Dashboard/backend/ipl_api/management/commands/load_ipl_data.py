# ipl_api/management/commands/load_ipl_data.py
import csv
from django.core.management.base import BaseCommand
from ipl_api.models import Match, Delivery
from datetime import datetime

class Command(BaseCommand):
    help = "Load matches.csv and deliveries.csv into DB"

    def add_arguments(self, parser):
        parser.add_argument('matches_csv', type=str)
        parser.add_argument('deliveries_csv', type=str)

    def handle(self, *args, **options):
        matches_csv = options['matches_csv']
        deliveries_csv = options['deliveries_csv']

        self.stdout.write("Loading matches...")
        Match.objects.all().delete()
        with open(matches_csv, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            bulk = []
            for row in reader:
                try:
                    date = datetime.strptime(row['date'], "%Y-%m-%d").date()
                except:
                    date = None
                bulk.append(Match(
                    match_id=int(row['id']),
                    season=int(row['season']),
                    city=row.get('city') or None,
                    date=date,
                    team1=row.get('team1'),
                    team2=row.get('team2'),
                    toss_winner=row.get('toss_winner'),
                    toss_decision=row.get('toss_decision'),
                    result=row.get('result'),
                    dl_applied=int(row.get('dl_applied') or 0),
                    winner=row.get('winner'),
                    win_by_runs=int(row.get('win_by_runs') or 0),
                    win_by_wickets=int(row.get('win_by_wickets') or 0),
                    venue=row.get('venue')
                ))
            Match.objects.bulk_create(bulk)
        self.stdout.write("Matches loaded.")

        self.stdout.write("Loading deliveries...")
        Delivery.objects.all().delete()
        with open(deliveries_csv, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            bulk = []
            batch = 2000
            for i, row in enumerate(reader, start=1):
                try:
                    match_ref = Match.objects.get(match_id=int(row['match_id']))
                except Match.DoesNotExist:
                    continue
                d = Delivery(
                    match=match_ref,
                    inning=int(row['inning']),
                    batting_team=row['batting_team'],
                    bowling_team=row['bowling_team'],
                    over=int(row['over']),
                    ball=int(row['ball']),
                    batsman=row['batsman'],
                    bowler=row['bowler'],
                    is_super_over=int(row.get('is_super_over') or 0),
                    wide_runs=int(row.get('wide_runs') or 0),
                    bye_runs=int(row.get('bye_runs') or 0),
                    legbye_runs=int(row.get('legbye_runs') or 0),
                    noball_runs=int(row.get('noball_runs') or 0),
                    penalty_runs=int(row.get('penalty_runs') or 0),
                    batsman_runs=int(row.get('batsman_runs') or 0),
                    extra_runs=int(row.get('extra_runs') or 0),
                    total_runs=int(row.get('total_runs') or 0),
                    player_dismissed=row.get('player_dismissed') or None,
                    dismissal_kind=row.get('dismissal_kind') or None,
                    fielder=row.get('fielder') or None
                )
                bulk.append(d)
                if i % batch == 0:
                    Delivery.objects.bulk_create(bulk)
                    bulk = []
            if bulk:
                Delivery.objects.bulk_create(bulk)
        self.stdout.write("Deliveries loaded.")
