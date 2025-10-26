from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),  # <-- root

    path('matches-per-year/', views.matches_per_year),
    path('wins-per-team-per-year/', views.wins_per_team_per_year),
    path('extra-runs/<int:year>/', views.extra_runs_per_team),
    path('top-economical/<int:year>/', views.top_economical_bowlers),
    path('matches-played-vs-won/<int:year>/', views.matches_played_vs_won),
]
