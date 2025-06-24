from flask import Flask, render_template_string, request
import pandas as pd
import math
import random

app = Flask(__name__)


movies = pd.DataFrame(
  {
    'title': [
        # Action
        'The Matrix', 'Inception', 'The Dark Knight', 'Mad Max: Fury Road', 'Gladiator',
        'John Wick', 'Die Hard',
        # Sci-Fi
        'Dune', 'Interstellar', 'Arrival', 'Blade Runner 2049', 'Ex Machina',
        # Thriller
        'Tenet', 'No Time to Die', 'Se7en', 'Gone Girl', 'Prisoners',
        # Crime
        'The Godfather', 'Pulp Fiction', 'The Departed', 'Heat', 'Joker',
        # Drama
        'Forrest Gump', 'The Shawshank Redemption', 'Oppenheimer', 'A Beautiful Mind', 'Parasite',
        # Animation
        'Toy Story', 'Finding Nemo', 'Soul', 'Turning Red', 'Coco',
        # Comedy
        'The Grand Budapest Hotel', 'Superbad', 'The Hangover', 'Step Brothers', 'Bridesmaids',
        # Family
        'The Lion King', 'Encanto', 'Paddington 2', 'The Incredibles', 'Frozen',
        # Adventure
        'Avatar: The Way of Water', 'Guardians of the Galaxy Vol. 3', 'Spider-Man: No Way Home', 'Jumanji: Welcome to the Jungle', 'Pirates of the Caribbean: The Curse of the Black Pearl',
        # Romance
        'La La Land', 'Pride & Prejudice', 'The Notebook', 'Titanic', 'Forrest Gump', 'After', 'Fifty Shades of Grey', 'Call Me by Your Name',
    ],
    'genres': [
        # Action
        'Action, Sci-Fi', 'Action, Sci-Fi, Thriller', 'Action, Crime, Drama', 'Action, Adventure, Sci-Fi', 'Action, Drama',
        'Action, Thriller, Crime', 'Action, Thriller',
        # Sci-Fi
        'Action, Adventure, Sci-Fi', 'Adventure, Drama, Sci-Fi', 'Drama, Sci-Fi', 'Action, Drama, Sci-Fi', 'Drama, Sci-Fi, Thriller',
        # Thriller
        'Action, Sci-Fi, Thriller', 'Action, Adventure, Thriller', 'Crime, Drama, Thriller', 'Drama, Mystery, Thriller', 'Crime, Drama, Thriller',
        # Crime
        'Crime, Drama', 'Crime, Drama', 'Crime, Drama, Thriller', 'Crime, Drama, Thriller', 'Crime, Drama, Thriller',
        # Drama
        'Drama, Romance', 'Drama', 'Biography, Drama, History', 'Biography, Drama', 'Drama, Thriller',
        # Animation
        'Animation, Comedy, Family', 'Animation, Adventure, Comedy', 'Animation, Adventure, Comedy', 'Animation, Comedy, Family', 'Animation, Adventure, Family',
        # Comedy
        'Comedy, Drama', 'Comedy', 'Comedy', 'Comedy', 'Comedy, Romance',
        # Family
        'Animation, Adventure, Drama', 'Animation, Comedy, Family', 'Animation, Adventure, Comedy', 'Animation, Adventure, Family', 'Animation, Adventure, Comedy',
        # Adventure
        'Action, Adventure, Sci-Fi', 'Action, Adventure, Comedy, Sci-Fi', 'Action, Adventure, Sci-Fi', 'Action, Adventure, Comedy', 'Action, Adventure, Fantasy',
        # Romance
        'Comedy, Drama, Music, Romance', 'Drama, Romance', 'Drama, Romance', 'Drama, Romance', 'Drama, Romance', 'Drama, Romance', 'Drama, Romance','Call Me by Your Name',
    ],
    'year': [
        # Action
        1999, 2010, 2008, 2015, 2000,
        2014, 1988,
        # Sci-Fi
        2021, 2014, 2016, 2017, 2014,
        # Thriller
        2020, 2021, 1995, 2014, 2013,
        # Crime
        1972, 1994, 2006, 1995, 2019,
        # Drama
        1994, 1994, 2023, 2001, 2019,
        # Animation
        1995, 2003, 2020, 2022, 2017,
        # Comedy
        2014, 2007, 2009, 2008, 2011,
        # Family
        1994, 2021, 2017, 2004, 2013,
        # Adventure
        2022, 2023, 2021, 2017, 2003,
        # Romance
        2016, 2005, 2004, 1997, 1994, 2019, 2015,2017,
    ]
  }
)

ALL_GENRES = [
    'Action', 'Sci-Fi', 'Thriller', 'Crime', 'Drama', 'Animation', 'Comedy', 'Family', 'Adventure', 'Romance'
]

QUOTE = "\"Movies touch our hearts and awaken our vision, and change the way we see things.\" – Martin Scorsese"
WELCOME = "Welcome! Discover your next favorite movie. Select the genres you love and get personalized recommendations."

HTML = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Movie Recommendation System</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
      min-height: 100vh;
      font-family: 'Segoe UI', 'Roboto', 'Arial', sans-serif;
      color: #22223b;
    }
    .navbar {
      background: #b8c6db !important;
      box-shadow: 0 2px 8px rgba(140, 120, 200, 0.08);
    }
    .navbar-brand {
      color: #22223b !important;
      font-weight: 600;
      letter-spacing: 1px;
      font-size: 1.5rem;
      text-shadow: 0 1px 4px rgba(255,255,255,0.15);
    }
    .card {
      max-width: 520px;
      margin: 40px auto;
      box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
      border-radius: 24px;
      border: none;
      background: rgba(255,255,255,0.96);
      backdrop-filter: blur(4px);
      color: #22223b;
    }
    .genre-list { columns: 2; -webkit-columns: 2; -moz-columns: 2; }
    .form-check-label {
      color: #22223b;
      font-weight: 500;
    }
    .form-check-input:checked {
      background-color: #b8c6db;
      border-color: #b8c6db;
    }
    .btn-primary {
      background-color: #a5c0dd;
      border: none;
      color: #22223b;
      font-weight: 600;
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(140, 120, 200, 0.10);
      transition: background 0.2s;
    }
    .btn-primary:hover {
      background-color: #b8c6db;
      color: #22223b;
    }
    .recommend-list { margin-top: 20px; }
    .list-group-item {
      background: #f3e8ff;
      border: none;
      color: #22223b;
      border-radius: 8px;
      margin-bottom: 6px;
      font-weight: 500;
    }
    .quote {
      font-style: italic;
      color: #4a4e69;
      margin-top: 20px;
      background: #f3e8ff;
      border-radius: 12px;
      padding: 10px 18px;
      box-shadow: 0 1px 4px rgba(140, 120, 200, 0.07);
    }
    .welcome {
      font-size: 1.1rem;
      color: #22223b;
      margin-bottom: 18px;
      background: #e0c3fc;
      border-radius: 10px;
      padding: 8px 0;
      box-shadow: 0 1px 4px rgba(140, 120, 200, 0.07);
      font-weight: 600;
    }
    h4, h5 {
      color: #22223b;
      font-weight: 700;
    }
    .alert-warning {
      background: #ffe0f7;
      color: #4a4e69;
      border: none;
      border-radius: 10px;
    }
    .btn-clear {
      background: #fff !important;
      color: #22223b !important;
      border: 1.5px solid #a5c0dd;
      font-weight: 600;
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(140, 120, 200, 0.10);
      transition: background 0.2s, color 0.2s;
    }
    .btn-clear:hover, .btn-clear:focus {
      background: #e0e0ef !important;
      color: #22223b !important;
      border-color: #a5c0dd;
    }
  </style>
</head>
<body>
  <nav class="navbar navbar-expand-lg mb-4">
    <div class="container-fluid">
      <span class="navbar-brand mb-0 h1 mx-auto" style="color:#22223b;">
        <span style="color:#FFD700;">🎬</span> Movie Recommendation System
      </span>
    </div>
  </nav>
  <div class="card p-4">
    <div class="welcome text-center">{{ welcome }}</div>
    <h4 class="mb-3 text-center">Choose your favorite genres</h4>
    <form method="post" id="genreForm">
      <div class="genre-list mb-3">
        {% for genre in genres %}
          <div class="form-check">
            <input class="form-check-input" type="checkbox" name="genres" value="{{ genre }}" id="{{ genre }}" {% if genre in selected_genres %}checked{% endif %}>
            <label class="form-check-label" for="{{ genre }}">{{ genre }}</label>
          </div>
        {% endfor %}
      </div>
      <div class="d-grid gap-2">
        <button type="submit" class="btn btn-primary">Get Recommendations</button>
        <button type="button" class="btn btn-clear" id="clearBtn">Clear Selection</button>
      </div>
    </form>
    {% if recommendations is none %}
      <div class="quote text-center">{{ quote }}</div>
    {% endif %}
    {% if recommendations is not none %}
      <div class="recommend-list">
        {% if selected_genres %}
          <div class="mb-2">You selected:
            {% for genre in selected_genres %}
              <span class="badge rounded-pill bg-primary" style="background-color:#a5c0dd;color:#22223b;font-weight:600;">{{ genre }}</span>
            {% endfor %}
          </div>
        {% endif %}
        <h5 class="mt-4">Recommended Movies:</h5>
        {% if recommendations %}
          <ul class="list-group">
          {% for movie in recommendations %}
            <li class="list-group-item">{{ movie }}</li>
          {% endfor %}
          </ul>
        {% else %}
          <div class="alert alert-warning mt-3">No movies found matching your preferences.</div>
        {% endif %}
      </div>
    {% endif %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  <script>
    document.getElementById('clearBtn').onclick = function() {
      window.location.href = window.location.pathname;
    };
  </script>
</body>
</html>
'''

def recommend_movies(preferred_genres, movies_df):
    recommendations = []
    seen_titles = set()
    for genre in preferred_genres:
        genre_matches = [
            (row['title'], row['year'])
            for _, row in movies_df.iterrows()
            if genre.lower() in [g.strip().lower() for g in row['genres'].split(',')]
        ]
        # Remove duplicates and already recommended
        genre_matches = [m for m in genre_matches if m[0] not in seen_titles]
        # Add all recommendations for this genre
        for m in genre_matches:
            recommendations.append(f"{m[0]} ({m[1]})")
            seen_titles.add(m[0])
    return recommendations

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    selected_genres = []
    if request.method == 'POST':
        selected_genres = request.form.getlist('genres')
        recommendations = recommend_movies(selected_genres, movies)
    return render_template_string(HTML, genres=ALL_GENRES, recommendations=recommendations, quote=QUOTE, welcome=WELCOME, selected_genres=selected_genres)

if __name__ == '__main__':
    app.run(debug=True) 