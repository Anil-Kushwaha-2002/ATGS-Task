# ipl_api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Sum
from collections import defaultdict
from .models import Match, Delivery

@api_view(['GET'])
def matches_per_year(request):
    qs = Match.objects.values('season').annotate(matches=Count('match_id')).order_by('season')
    data = [{"season": r['season'], "matches": r['matches']} for r in qs]
    return Response(data)

@api_view(['GET'])
def wins_per_team_per_year(request):
    qs = Match.objects.values('season', 'winner').annotate(wins=Count('winner')).order_by('season')
    seasons = defaultdict(dict)
    teams = set()
    for r in qs:
        winner = r['winner'] or 'No Result'
        seasons[r['season']][winner] = r['wins']
        if r['winner']:
            teams.add(r['winner'])
    out = []
    for season in sorted(seasons.keys()):
        out.append({"season": season, "team_wins": seasons[season]})
    return Response({"seasons": out, "teams": sorted(list(teams))})

@api_view(['GET'])
def extra_runs_per_team(request, year: int):
    match_ids = Match.objects.filter(season=year).values_list('match_id', flat=True)
    qs = Delivery.objects.filter(match__match_id__in=match_ids).values('bowling_team').annotate(extra_runs=Sum('extra_runs')).order_by('bowling_team')
    data = [{"team": r['bowling_team'], "extra_runs": r['extra_runs']} for r in qs]
    return Response(data)

@api_view(['GET'])
def top_economical_bowlers(request, year: int):
    match_ids = Match.objects.filter(season=year).values_list('match_id', flat=True)
    qs = Delivery.objects.filter(match__match_id__in=match_ids).values('bowler').annotate(total_runs=Sum('total_runs'), balls=Count('id'))
    results = []
    for r in qs:
        balls = r['balls'] or 0
        if balls < 6:
            continue
        overs = balls / 6.0
        economy = (r['total_runs'] or 0) / overs if overs > 0 else None
        results.append({"bowler": r['bowler'], "total_runs": r['total_runs'], "balls": balls, "economy": round(economy, 2) if economy else None})
    results_sorted = sorted(results, key=lambda x: x['economy'])[:20]
    return Response(results_sorted)

@api_view(['GET'])
def matches_played_vs_won(request, year:int):
    matches = Match.objects.filter(season=year)
    played = {}
    for m in matches:
        played[m.team1] = played.get(m.team1, 0) + 1
        played[m.team2] = played.get(m.team2, 0) + 1
    wins_qs = matches.values('winner').annotate(wins=Count('winner'))
    wins = {r['winner']: r['wins'] for r in wins_qs if r['winner']}
    teams = sorted(set(list(played.keys()) + list(wins.keys())))
    data = [{"team": t, "played": played.get(t,0), "won": wins.get(t,0)} for t in teams]
    return Response(data)
