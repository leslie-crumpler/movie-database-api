"""
models.py - Movie data access with filtering and pagination
"""

from database import get_connection


class MovieModel:
    @staticmethod
    def get_all(genre=None, year=None, page=1, limit=10):
        conn = get_connection()
        query = "SELECT * FROM movies WHERE 1=1"
        params = []

        if genre:
            query += " AND genre = ?"
            params.append(genre)
        if year:
            query += " AND year = ?"
            params.append(int(year))

        # Pagination
        offset = (page - 1) * limit
        query += " ORDER BY rating DESC LIMIT ? OFFSET ?"
        params += [limit, offset]

        movies = conn.execute(query, params).fetchall()
        conn.close()
        return [dict(m) for m in movies]

    @staticmethod
    def get_by_id(movie_id):
        conn = get_connection()
        movie = conn.execute("SELECT * FROM movies WHERE id = ?", (movie_id,)).fetchone()
        conn.close()
        return dict(movie) if movie else None

    @staticmethod
    def create(title, genre, year, rating, description):
        if not title or not title.strip():
            raise ValueError("Title is required.")
        if rating is not None and not (0.0 <= float(rating) <= 10.0):
            raise ValueError("Rating must be between 0 and 10.")
        conn = get_connection()
        cursor = conn.execute(
            "INSERT INTO movies (title, genre, year, rating, description) VALUES (?,?,?,?,?)",
            (title.strip(), genre, year, rating, description)
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    @staticmethod
    def update(movie_id, data):
        conn = get_connection()
        fields = []
        params = []
        for key in ["title", "genre", "year", "rating", "description"]:
            if key in data:
                fields.append(f"{key} = ?")
                params.append(data[key])
        if not fields:
            conn.close()
            return False
        params.append(movie_id)
        conn.execute(f"UPDATE movies SET {', '.join(fields)} WHERE id = ?", params)
        conn.commit()
        conn.close()
        return True

    @staticmethod
    def delete(movie_id):
        conn = get_connection()
        conn.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
        conn.commit()
        conn.close()
