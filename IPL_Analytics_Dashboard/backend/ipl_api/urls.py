# ipl_api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('matches_per_year/', views.matches_per_year, name='matches_per_year'),
    path('wins_per_team_per_year/', views.wins_per_team_per_year, name='wins_per_team_per_year'),
    path('extra_runs_per_team/<int:year>/', views.extra_runs_per_team, name='extra_runs_per_team'),
    path('top_economical_bowlers/<int:year>/', views.top_economical_bowlers, name='top_economical_bowlers'),
    path('matches_played_vs_won/<int:year>/', views.matches_played_vs_won, name='matches_played_vs_won'),
]
