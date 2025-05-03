import streamlit as st
import requests
import subprocess
import os
import time

# --- Configuration ---
BACKEND_URL = "http://127.0.0.1:5000/recommendations"
BACKEND_SCRIPT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "backend", "api.py")

# --- Function to start the backend as a subprocess ---
def start_backend():
    if not is_backend_running():
        st.info("Starting backend server...")
        try:
            subprocess.Popen(["python", BACKEND_SCRIPT])
            time.sleep(2)  # Give the backend a moment to start
            if is_backend_running():
                st.success("Backend server started successfully!")
            else:
                st.error("Failed to start backend server.")
        except Exception as e:
            st.error(f"Error starting backend: {e}")

# --- Function to check if the backend is running ---
def is_backend_running():
    try:
        requests.get(BACKEND_URL)
        return True
    except requests.exceptions.ConnectionError:
        return False

# Page settings
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# App title
st.markdown(
    """
    <h1 style='text-align: center; color: #ff4b4b;'>🎬 Movie Recommender System</h1>
    <p style='text-align: center;'>Find your next favorite movie!</p>
    """,
    unsafe_allow_html=True
)

# --- Start the backend when the app runs ---
start_backend()

# --- Recommend Function (Connects to Backend API) ---
def recommend(movie_name=None):
    headers = {'Content-Type': 'application/json'}
    data = {'movie_title': movie_name}

    try:
        response = requests.post(BACKEND_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        recommendations_data = response.json()
        if "recommendations" in recommendations_data:
            return recommendations_data["recommendations"]
        elif "error" in recommendations_data:
            st.error(f"Backend Error: {recommendations_data['error']}")
            return []
        else:
            st.warning("No recommendations received from backend.")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to backend: {e}")
        return []

# --- SEARCH BAR ---
movie_name = st.text_input("🔎 Search for a movie:", "")

# --- Decide What to Show ---
if movie_name:
    st.markdown("---")
    st.subheader(f"🎯 Recommendations based on: **{movie_name}**")
    recommended_movies = recommend(movie_name)
    if recommended_movies:
        # --- Show Recommended Movies ---
        cols = st.columns(5)
        for idx, movie_title in enumerate(recommended_movies):
            with cols[idx % 5]:
                st.markdown(f"<h5 style='text-align: center; color: #00adb5;'>{movie_title}</h5>", unsafe_allow_html=True)
                if st.button("❤️ Add to Favorites", key=f"fav_{movie_title}"):
                    st.success(f"Added {movie_title} to favorites!")
    else:
        st.info("No recommendations found for the entered movie.")

else:
    st.markdown("---")
    st.subheader("🔥 Enter a movie title to get recommendations!")