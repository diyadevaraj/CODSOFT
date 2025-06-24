import pandas as pd

# Hardcoded dataset of movies and genres
movies = pd.DataFrame({
    'title': [
        'The Matrix', 'Inception', 'The Godfather', 'Toy Story', 'The Dark Knight',
        'Pulp Fiction', 'Finding Nemo', 'The Shawshank Redemption', 'The Lion King', 'Forrest Gump'
    ],
    'genres': [
        'Action, Sci-Fi', 'Action, Sci-Fi, Thriller', 'Crime, Drama', 'Animation, Comedy, Family',
        'Action, Crime, Drama', 'Crime, Drama', 'Animation, Adventure, Comedy',
        'Drama', 'Animation, Adventure, Drama', 'Drama, Romance'
    ]
})

def get_user_preferences():
    print("Available genres: Action, Sci-Fi, Thriller, Crime, Drama, Animation, Comedy, Family, Adventure, Romance")
    user_input = input("Enter your favorite genres (comma separated): ")
    preferred_genres = [genre.strip().lower() for genre in user_input.split(',')]
    return preferred_genres

def recommend_movies(preferred_genres, movies_df):
    recommendations = []
    for _, row in movies_df.iterrows():
        movie_genres = [g.strip().lower() for g in row['genres'].split(',')]
        if any(genre in movie_genres for genre in preferred_genres):
            recommendations.append(row['title'])
    return recommendations

def main():
    preferred_genres = get_user_preferences()
    recommendations = recommend_movies(preferred_genres, movies)
    print("\nRecommended Movies:")
    if recommendations:
        for movie in recommendations:
            print(f"- {movie}")
    else:
        print("No movies found matching your preferences.")

if __name__ == "__main__":
    main() 