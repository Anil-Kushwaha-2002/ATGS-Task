# IPL Analytics API

This is a **Django REST Framework** project that provides APIs for analyzing IPL (Indian Premier League) cricket data. 
It uses CSV datasets for matches and deliveries and provides endpoints to get insights like matches per year, team wins, extra runs, top economical bowlers, and matches played vs won.

---

# IPL Dashboard Project

A full-stack IPL (Indian Premier League) dashboard project with **Django REST API backend** and **ReactJS frontend**.  
It provides various IPL statistics, such as matches per year, team wins, extra runs, top economical bowlers, and matches played vs won.


## Project Structure
```bash
ipl_analytics_dashboard/
├─ backend/
│  ├─ manage.py
│  ├─ backend/                # django project
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  └─ ...
│  ├─ ipl_api/                # django app
│  │  ├─ models.py
│  │  ├─ serializers.py
│  │  ├─ views.py
│  │  ├─ urls.py
│  │  ├─ management/commands/load_ipl.py
│  │  └─ ...
│  ├─ requirements.txt
│  └─ data/
│     ├─ matches.csv
│     └─ deliveries.csv
└─ frontend/
   ├─ package.json
   ├─ src/
   │  ├─ App.jsx
   │  ├─ index.js
   │  ├─ pages/
   │  │  ├─ Landing.jsx
   │  │  ├─ ExtraRuns.jsx
   │  │  ├─ TopEconomical.jsx
   │  │  └─ MatchesPlayedVsWon.jsx
   │  └─ components/
   │     └─ ChartWrapper.jsx
   └─ README.md
```


---

## Features / API Endpoints

The project exposes the following API endpoints:
```bash
| Endpoint | Description |
| -------- | ----------- |
| `GET /` | Home route with welcome message and available endpoints |
| `GET /api/matches-per-year/` | Get number of matches played each season |
| `GET /api/wins-per-team-per-year/` | Get wins per team per season (stacked data) |
| `GET /api/extra-runs/<year>/` | Get total extra runs conceded by each team for a given year |
| `GET /api/top-economical/<year>/?top=10` | Get top economical bowlers for a given year (default top 10) |
| `GET /api/matches-played-vs-won/<year>/` | Get matches played vs won per team for a given year |
| `GET /admin/` | Django admin panel |
```
---
## Features

- **Matches per year**
- **Wins per team per year**
- **Extra runs per year**
- **Top economical bowlers per year**
- **Matches played vs won per year**
- **Dark mode charts with Chart.js**
- Responsive frontend using **ReactJS** and **MUI**
- Axios-based API integration with Django REST backend

## Technologies Used
```bash
Python 3.13
Django 5.2
Django REST Framework 3.15
Pandas 2.2
SQLite (default DB, PostgreSQL optional)
Frontend: ReactJS (optional for visualizations)
```

## Backend API endpoints:
```bash
Purpose	                               URL
Matches per year                 	/api/matches-per-year/
Wins per team per year	            /api/wins-per-team-per-year/
Extra runs in a year (e.g.,2016)	   /api/extra-runs/2016/
Top economical bowlers in a year	   /api/top-economical/2015/
Matches played vs won (e.g.,2017)	/api/matches-played-vs-won/2017/
```

## Installation Setup

### Backend Setup 
```bash
1. Clone the repository:
git clone <repo-url>
cd ipl_analytics_dashboard/backend

2. Create and activate a virtual environment:
python -m venv venv
.\venv\Scripts\activate     # Windows
# source venv/bin/activate  # Linux / Mac

3. Install dependencies:
```base
pip install -r requirements.txt

4. Run migrations:
python manage.py migrate

5. Load IPL CSV data:
python manage.py load_ipl

6. Start the development server:
python manage.py runserver

7. Open your browser at http://127.0.0.1:8000/ to see the API home.
```
### Frontend Setup (ReactJS)
```bash
1. Navigate to the frontend directory:
cd cd ipl_analytics_dashboard/frontend

2. Install dependencies:
npm install
npm install @mui/material @emotion/react @emotion/styled react-router-dom react-chartjs-2 chart.js axios

3. Start the React development server:
npm start

Frontend runs at: http://localhost:3000
Ensure your Django backend is running at http://127.0.0.1:8000 for API calls.
```
## Notes
Use `django-cors-headers` to allow frontend to communicate with backend:
```bash
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # For development only
```