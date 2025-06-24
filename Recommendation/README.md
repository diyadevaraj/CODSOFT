🎬 Movie Recommendation System

A simple, interactive web application built with Flask that helps users discover movies based on their favorite genres. The system provides personalized movie recommendations from a curated dataset, all within a modern, user-friendly interface.

🔧Features:

    🎯 Genre-Based Recommendations: Select one or more genres (Action, Sci-Fi, Thriller, Crime, Drama, Animation, Comedy, Family, Adventure, Romance) to receive a list of recommended movies.
    
    🎥 Curated Movie Dataset: The app uses a built-in dataset of popular and critically acclaimed movies, each tagged with genres and release years.
    
    ✨ Modern UI: Clean, responsive interface styled with Bootstrap for a pleasant user experience.
    
    ⚡ Instant Results: Recommendations are generated instantly based on your selected genres—no need to sign up or log in.
    
    🔄 Easy Reset: Clear your selections at any time to start a new search.
    
How It Works

    📝 Select Genres: On the homepage, choose your favorite genres from the list.

    🎬 Get Recommendations: Click "Get Recommendations" to see a list of movies matching your preferences.
    
    🧹 Clear Selection: Use the "Clear Selection" button to reset your choices and start over.
    
Tech Stack
    🐍 Backend: Python, Flask
    🖥️ Frontend: HTML, Bootstrap (via CDN)
    🗂️ Data: Pandas DataFrame (in-memory, no external database required)
    
Getting Started

    1.📥 Clone the repository:  git clone https://github.com/yourusername/your-repo-name.git
                                cd your-repo-name/Recommendation
                              
    2.📦 Install dependencies: pip install -r requirements.txt
    
    3.🚀 Run the app: python app.py
       
The app will be available at http://127.0.0.1:5000/

File Structure:

    📁 app.py — Main Flask application with UI and recommendation logic
    📁 recommendation_system.py — (If present) Additional logic or utilities for recommendations
    📄 requirements.txt — Python dependencies
