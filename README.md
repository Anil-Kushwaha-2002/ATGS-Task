# ATGS-Task
# 🏏 IPL Analytics Dashboard

- An interactive IPL Data Analytics Dashboard built using Django (backend) and ReactJS (frontend).
- It visualizes IPL statistics such as matches per year, team wins, and top economical bowlers with beautiful charts.
- IPL Analytics Dashboard is a full-stack web application built using Django (REST API) and ReactJS, designed to visualize and analyze Indian Premier League (IPL) data such as matches per year, team wins, extra runs, and economical bowlers.
- It processes large CSV datasets and provides interactive dashboards with beautiful charts.

# 🚀 Project Overview

- This project analyzes IPL match and delivery data from CSV files and provides RESTful APIs for insights.
The React frontend consumes these APIs to display interactive charts (via Chart.js / MUI).

# 🧩 Tech Stack
```bash
Frontend  	ReactJS, Axios, Chart.js, Material-UI
Backend	    Django, Django REST Framework
Database	  SQLite (default)
Language	  Python 3.x, JavaScript (ES6)
```

# ⚙️ Setup Instructions

### Backend Setup (Django)
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)
# or
source venv/bin/activate  # (Linux/macOS)

pip install -r requirements.txt
python manage.py migrate

Run the Backend Server
python manage.py runserver


API will be available at:

http://127.0.0.1:8000/api/
```
️### Frontend Setup (React)
```bash
Open a new terminal:

cd frontend
npm install
npm start


Frontend will run on:

http://localhost:3000/
```
# 🧠 Available API Endpoints

| Endpoint                             | Description                                       |
| ------------------------------------ | ------------------------------------------------- |
| `/api/matches-per-year/`             | Returns total matches played each season          |
| `/api/wins-per-team-per-year/`       | Returns stacked win data for teams across seasons |
| `/api/top-economical/<year>/?top=10` | Returns top economical bowlers for a given year   |
/*
---
---

# Thumbnail_Pipeline
📘 Overview

- Thumbnail Pipeline is an automated image processing pipeline that generates optimized thumbnails from images or videos using Python.
It ensures efficient image resizing, compression, and format conversion for use in web platforms or applications.

# 🚀 Features

- 🧩 Batch thumbnail generation
- ⚙️ Supports multiple formats (JPG, PNG, WEBP)
- 🖼️ Auto-resize and optimize images
- 📁 Handles large image folders automatically
- 🧠 Modular design for pipeline integration

@ 🧩 Tech Stack
```bash
Language    	Python 3.x
Libraries	    Pillow, OpenCV, os, argparse
Output      	Optimized thumbnails in /output directory
```

# ⚙️ Setup Instructions
```bash
1️⃣ Clone Repository
git clone https://github.com/<your-username>/Thumbnail_Pipeline.git
cd Thumbnail_Pipeline

2️⃣ Install Dependencies
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate
pip install -r requirements.txt

3️⃣ Run the Thumbnail Generator
python pipeline.py --input input --output output --size 300x300


✅ Example Output:

Processing 10 images...
✅ sample1.jpg → sample1_thumb.jpg
✅ sample2.png → sample2_thumb.png
All thumbnails generated successfully in /output/
```
