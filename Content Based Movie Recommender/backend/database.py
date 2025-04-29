import sqlite3
from typing import List, Dict, Any

DB_NAME = "movies.db"

def get_connection() -> sqlite3.Connection:
    """
    Opens a SQLite connection to the database file.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables() -> None:
    """
    Creates the necessary tables if they do not already exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Movies table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Movies (
        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER,
        description TEXT
    )
    ''')

    # Genres table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Genres (
        genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
        genre_name TEXT UNIQUE NOT NULL
    )
    ''')

    # MovieGenres join table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS MovieGenres (
        movie_id INTEGER,
        genre_id INTEGER,
        PRIMARY KEY (movie_id, genre_id),
        FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
        FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
    )
    ''')

    # FavoriteMovies table (only one user)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS FavoriteMovies (
        movie_id INTEGER PRIMARY KEY,
        FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
    )
    ''')

    conn.commit()
    conn.close()


def add_movie(title: str, release_year: int, description: str) -> int:
    """
    Inserts a new movie and returns its generated movie_id.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO Movies (title, release_year, description) VALUES (?, ?, ?)',
        (title, release_year, description)
    )
    conn.commit()
    movie_id = cursor.lastrowid
    conn.close()
    return movie_id


def get_all_movies() -> List[Dict[str, Any]]:
    """
    Returns a list of all movies in the database as dictionaries.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Movies')
    rows = cursor.fetchall()
    conn.close()
    # Convert sqlite3.Row to dict
    return [dict(row) for row in rows]


def add_genre(name: str) -> int:
    """
    Inserts a new genre if it doesn't exist and returns its id.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO Genres (genre_name) VALUES (?)', (name,))
    conn.commit()
    cursor.execute('SELECT genre_id FROM Genres WHERE genre_name = ?', (name,))
    genre_id = cursor.fetchone()[0]
    conn.close()
    return genre_id


def assign_genre(movie_id: int, genre_id: int) -> None:
    """
    Associates a movie with a genre.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT OR IGNORE INTO MovieGenres (movie_id, genre_id) VALUES (?, ?)',
        (movie_id, genre_id)
    )
    conn.commit()
    conn.close()


def get_genres_for_movie(movie_id: int) -> List[str]:
    """
    Returns a list of genre names for a given movie.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT g.genre_name
        FROM Genres g
        JOIN MovieGenres mg ON g.genre_id = mg.genre_id
        WHERE mg.movie_id = ?
        ''', (movie_id,)
    )
    results = [row['genre_name'] for row in cursor.fetchall()]
    conn.close()
    return results


def get_movies_by_genre(genre_id: int) -> List[Dict[str, Any]]:
    """
    Returns all movies associated with a specific genre_id as dictionaries.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT m.*
        FROM Movies m
        JOIN MovieGenres mg ON m.movie_id = mg.movie_id
        WHERE mg.genre_id = ?
        ''', (genre_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def add_favorite(movie_id: int) -> None:
    """
    Marks a movie as favorite (for the single user).
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT OR IGNORE INTO FavoriteMovies (movie_id) VALUES (?)',
        (movie_id,)
    )
    conn.commit()
    conn.close()


def remove_favorite(movie_id: int) -> None:
    """
    Removes a movie from favorites.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM FavoriteMovies WHERE movie_id = ?', (movie_id,))
    conn.commit()
    conn.close()


def get_favorites() -> List[Dict[str, Any]]:
    """
    Returns a list of the user's favorite movies as dictionaries.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT m.*
        FROM Movies m
        JOIN FavoriteMovies f ON m.movie_id = f.movie_id
        '''
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
