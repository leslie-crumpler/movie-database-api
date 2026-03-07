"""
database.py - Setup and connection for Movie Database API
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../movies.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT,
            year INTEGER,
            rating REAL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Seed sample data if empty
    count = conn.execute("SELECT COUNT(*) FROM movies").fetchone()[0]
    if count == 0:
        sample_movies = [
            ("The Matrix", "Sci-Fi", 1999, 8.7, "A hacker discovers the truth about reality."),
            ("Inception", "Sci-Fi", 2010, 8.8, "A thief who enters dreams to steal secrets."),
            ("The Dark Knight", "Action", 2008, 9.0, "Batman faces the Joker in Gotham City."),
            ("Parasite", "Thriller", 2019, 8.5, "A poor family schemes to work for a wealthy household."),
            ("Interstellar", "Sci-Fi", 2014, 8.6, "Astronauts travel through a wormhole to save humanity."),
        ]
        conn.executemany(
            "INSERT INTO movies (title, genre, year, rating, description) VALUES (?,?,?,?,?)",
            sample_movies
        )
    conn.commit()
    conn.close()
    print("Movie database initialized.")
