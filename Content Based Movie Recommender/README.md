# Movie Recommendation System

This project implements a movie recommendation system with a Flask backend serving recommendations from a pre-trained model and a Streamlit frontend providing a user interface to interact with the backend.

## Overview

The system uses a machine learning model (likely based on techniques like TF-IDF and cosine similarity, trained on movie data) to generate recommendations based on user input. The backend exposes an API endpoint that the frontend can query to retrieve these recommendations.

## Project Structure

The project directory structure is as follows:
├── backend/
│   ├── pycache/
│   ├── init.py
│   ├── api.py          # Flask backend application
│   ├── build_model.py  # Script to build and save the recommendation model
│   ├── movie_recommendation_model.pkl # Pre-trained recommendation model file
│   └── requirements.txt # Backend dependencies
├── frontend/
│   └── app.py          # Streamlit frontend application
│   └── requirements.txt # Frontend dependencies
├── .gitignore
├── README.md         # This file
├── tmdb_5000_credits.csv   # Movie credits dataset (likely used for model training)
└── tmdb_5000_movies.csv    # Movie details dataset (likely used for model training)


## Prerequisites

* **Python:** Version 3.6 or higher is recommended. You can check your Python version by running `python --version` or `python3 --version` in your terminal.
* **pip:** The Python package installer. It usually comes bundled with Python. You can check if you have pip installed by running `pip --version` in your terminal.
* **Virtual Environment (Optional but Recommended):** Using a virtual environment helps to isolate project dependencies.

## Installation

1.  **Clone the Repository:**

    If you haven't already, clone the project repository to your local machine:

    ```bash
    git clone <your_repository_url>
    cd Movies-Recommendation-System-main
    ```

2.  **Create a Virtual Environment (Recommended):**

    Navigate to the project root directory and create a virtual environment:

    ```bash
    python -m venv venv  # For venv
    # Or, if you prefer Conda:
    # conda create -n movie_recommender python=3.8
    # conda activate movie_recommender
    ```

    Activate the virtual environment:

    ```bash
    source venv/bin/activate  # On Linux/macOS (for venv)
    venv\Scripts\activate  # On Windows (for venv)
    conda activate movie_recommender # For Conda
    ```

3.  **Install Backend Dependencies:**

    Navigate to the `backend` directory and install the required Python packages:

    ```bash
    cd backend
    pip install -r requirements.txt
    ```

    This will install Flask, Flask-CORS, pandas, scikit-learn, and any other libraries listed in the `requirements.txt` file.

4.  **Install Frontend Dependencies:**

    Navigate to the `frontend` directory and install the required Python packages:

    ```bash
    cd frontend
    pip install -r requirements.txt
    ```

    This will install Streamlit and the `requests` library.

## Running the Application

The backend (Flask API) and the frontend (Streamlit UI) need to be run separately.

1.  **Start the Backend (Flask API):**

    * Open a **new** terminal or command prompt.
    * Navigate to the `backend` directory:

        ```bash
        cd backend
        ```

    * Run the Flask API script:

        ```bash
        python api.py
        ```

        You should see output indicating that the Flask development server has started, usually running at `http://127.0.0.1:5000`. **Keep this terminal window running in the background.**

2.  **Start the Frontend (Streamlit UI):**

    * Open **another new** terminal or command prompt.
    * Navigate to the `frontend` directory:

        ```bash
        cd frontend
        ```

    * Run the Streamlit application. **Important:** Replace the path in the command below with the actual path to your `app.py` file if it's different.

        ```bash
        python -m streamlit run app.py
        ```

        For example, if your full path is `e:/Movies-Recommendation-System-main/Movies-Recommendation-System-main/frontend/app.py`, the command would be:

        ```bash
        python -m streamlit run e:/Movies-Recommendation-System-main/Movies-Recommendation-System-main/frontend/app.py
        ```

        Streamlit will then start a development server and automatically open your movie recommendation system in a web browser. You can interact with the UI in the browser to search for movies and get recommendations from the backend.

## Troubleshooting

* **Backend Connection Errors (Frontend):** If you see errors in your Streamlit app related to connecting to `http://127.0.0.1:5000`, ensure that the Flask backend is running correctly in its separate terminal. Check the backend terminal for any error messages.
* **Streamlit Command Not Found:** If the `streamlit run` command fails, it means Streamlit is not accessible in your current terminal session. Ensure your virtual environment (if used) is activated or that Streamlit's installation directory is in your system's PATH. You can also try running it using `python -m streamlit run <path_to_app.py>`.
* **Import Errors:** If either the backend or frontend scripts fail with `ModuleNotFoundError`, it indicates that the required libraries are not installed in the active Python environment. Double-check that you ran `pip install -r requirements.txt` in both the `backend` and `frontend` directories while the virtual environment was active.
* **Model Loading Errors (Backend):** If the backend fails to start or gives errors about not loading the `movie_recommendation_model.pkl` file, ensure that this file exists in the `backend` directory and that the path in `api.py` is correct. You might need to re-run the `build_model.py` script (located in the `backend` directory) to generate this file if it's missing or outdated.
