# 🎬 Movie Recommender System

A simple **Streamlit** web app powered by **Machine Learning** and **SQLite** to recommend movies based on user input!

---

## 🚀 Features
- Recommend movies based on plot similarity.
- Search for a movie and get a list of similar titles.
- Backend with SQLite for structured storage.
- Frontend with Streamlit for fast and interactive UI.

---

## 🛠 Project Structure

```
movie_recommender/
│
├── backend/
│   ├── database.py         # SQLite database setup and helpers
│   ├── recommender.py      # ML model for movie recommendations
│   └── __init__.py         # Module initializer
│
├── frontend/
│   └── app.py              # Streamlit frontend app
│
├── tmdb_5000_movies.csv    # Raw movie dataset
├── tmdb_5000_credits.csv   # Raw credits dataset
├── README.md
├── requirements.txt        # App requirements
└── model.db                # SQLite database
```

---

## 📦 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/movie_recommender.git
   cd movie_recommender
   ```

2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run frontend/app.py
   ```

4. **Access the app:**
   Open your browser at [http://localhost:8501](http://localhost:8501)

---

## 📄 Requirements
- Python 3.8+
- pandas
- scikit-learn
- sqlite3 (built-in)
- streamlit

## 📊 Dataset
- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Includes movie metadata and credits (actors, directors, etc.)

---

## ✨ Acknowledgements
- TMDB for the dataset.
- Streamlit for making web apps easy and fun.

---

## 📬 Contact
If you have any questions or suggestions, feel free to reach out!

