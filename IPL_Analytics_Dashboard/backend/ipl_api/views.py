# ipl_api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Sum, F, FloatField
from django.db.models import Q
from .models import Match, Delivery
from django.db.models import Avg
from django.http import JsonResponse


# ---------------------------
# Home / Project Landing Page
# ---------------------------
def home(request):
    return JsonResponse({
        "message": "Welcome to IPL API project",
        "available_routes": [
            "/api/matches-per-year/",
            "/api/wins-per-team-per-year/",
            "/api/extra-runs/<year>/",
            "/api/top-economical/<year>/?top=10",
            "/api/matches-played-vs-won/<year>/",
            "/admin/"
        ]
    })

# ---------------------------
# API Landing Page
# ---------------------------
def api_home(request):
    return JsonResponse({
        "message": "Welcome to IPL API",
        "endpoints": [
            "matches-per-year/",
            "wins-per-team-per-year/",
            "extra-runs/<year>/",
            "top-economical/<year>/?top=10",
            "matches-played-vs-won/<year>/"
        ]
    })


# ---------------------------
# API Endpoints
# ---------------------------

@api_view(['GET'])
def matches_per_year(request):
    qs = Match.objects.values('season').annotate(matches=Count('id')).order_by('season')
    data = [{'season': r['season'], 'matches': r['matches']} for r in qs]
    return Response(data)

@api_view(['GET'])
def wins_per_team_per_year(request):
    # For stacked bar: for each season, each team and wins count
    qs = Match.objects.exclude(winner='').values('season', 'winner').annotate(wins=Count('id')).order_by('season')
    # convert into structure {season: {team: wins}}
    result = {}
    teams = set()
    for r in qs:
        season = r['season']
        team = r['winner']
        wins = r['wins']
        teams.add(team)
        result.setdefault(season, {})[team] = wins
    seasons = sorted(result.keys())
    teams = sorted(list(teams))
    payload = {
        'seasons': seasons,
        'teams': teams,
        'data': {s: [ result[s].get(t, 0) for t in teams ] for s in seasons}
    }
    return Response(payload)

@api_view(['GET'])
def extra_runs_per_team(request, year: int):
    # deliveries joined with matches -> filter matches season==year, then sum extra_runs grouped by bowling_team
    qs = Delivery.objects.filter(match__season=year).values('bowling_team').annotate(extra_runs=Sum('extra_runs')).order_by('-extra_runs')
    data = [{'team': r['bowling_team'], 'extra_runs': r['extra_runs'] or 0} for r in qs]
    return Response({'year': year, 'teams': data})

@api_view(['GET'])
def top_economical_bowlers(request, year: int):
    # For economy: economy = total_runs_conceded / overs_bowled (overs_bowled = balls/6). We'll compute total_runs and balls per bowler for that year (match__season=year)
    top = int(request.GET.get('top', 10))
    # annotate ball count and runs per bowler
    from django.db.models import Count
    qs = Delivery.objects.filter(match__season=year).values('bowler').annotate(
        balls=Count('id'),
        runs=Sum('total_runs')
    ).filter(balls__gte=6).order_by()  # at least 1 over bowled
    # compute economy on Python side to avoid division by zero issues:
    results = []
    for r in qs:
        balls = r['balls'] or 0
        overs = balls / 6.0 if balls > 0 else 0.0
        economy = (r['runs'] or 0) / overs if overs > 0 else None
        results.append({'bowler': r['bowler'], 'balls': balls, 'runs': r['runs'] or 0, 'economy': round(economy, 3) if economy is not None else None})
    results_sorted = sorted([x for x in results if x['economy'] is not None], key=lambda x: x['economy'])[:top]
    return Response({'year': year, 'top': top, 'bowlers': results_sorted})

@api_view(['GET'])
def matches_played_vs_won(request, year: int):
    # matches played per team in that season (as team1 or team2), and matches won (winner)
    matches_qs = Match.objects.filter(season=year)
    # played: count occurrences where team is team1 or team2
    teams = set()
    for m in matches_qs:
        if m.team1: teams.add(m.team1)
        if m.team2: teams.add(m.team2)
    data = []
    for team in sorted(teams):
        played = matches_qs.filter(Q(team1=team) | Q(team2=team)).count()
        won = matches_qs.filter(winner=team).count()
        data.append({'team': team, 'played': played, 'won': won})
    return Response({'year': year, 'data': data})




# We’ll create endpoints for all the tasks:

# / → Homepage JSON
# /api/ → API landing JSON
# /api/matches-per-year/ → Task 1 --> matches per year
# /api/wins-per-team-per-year/ → Task 2 (stacked) --> 
# /api/extra-runs/<int:year>/ → Task 3  --> extra runs for 2016
# /api/top-economical/<int:year>/?top=10 → Task 4
# /api/matches-played-vs-won/<int:year>/ → Task 5

"""
# Try visiting one of these endpoints:-

Purpose	                                              Example URL
Matches per year                            	http://127.0.0.1:8000/api/matches-per-year/
Wins per team per year                      	http://127.0.0.1:8000/api/wins-per-team-per-year/
Extra runs in a year (e.g. 2016)	            http://127.0.0.1:8000/api/extra-runs/2016/
Top economical bowlers in a year (e.g. 2015)	http://127.0.0.1:8000/api/top-economical/2015/
Matches played vs won (e.g. 2017)	            http://127.0.0.1:8000/api/matches-played-vs-won/2017/

"""