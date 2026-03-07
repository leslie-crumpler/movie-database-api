"""
app.py - Movie Database REST API
Demonstrates: REST endpoints, filtering, pagination, error handling
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, request, jsonify
from database import init_db
from models import MovieModel

app = Flask(__name__)


# ── Movie Routes ─────────────────────────────────────────

@app.route("/movies", methods=["GET"])
def list_movies():
    genre = request.args.get("genre")
    year = request.args.get("year")
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    if page < 1 or limit < 1 or limit > 100:
        return jsonify({"error": "Invalid pagination parameters."}), 400

    movies = MovieModel.get_all(genre=genre, year=year, page=page, limit=limit)
    return jsonify({
        "page": page,
        "limit": limit,
        "count": len(movies),
        "movies": movies
    })


@app.route("/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movie = MovieModel.get_by_id(movie_id)
    if not movie:
        return jsonify({"error": "Movie not found."}), 404
    return jsonify(movie)


@app.route("/movies", methods=["POST"])
def add_movie():
    data = request.get_json()
    try:
        new_id = MovieModel.create(
            title=data.get("title", ""),
            genre=data.get("genre"),
            year=data.get("year"),
            rating=data.get("rating"),
            description=data.get("description", "")
        )
        return jsonify({"message": "Movie added.", "id": new_id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    if not MovieModel.get_by_id(movie_id):
        return jsonify({"error": "Movie not found."}), 404
    data = request.get_json()
    MovieModel.update(movie_id, data)
    return jsonify({"message": "Movie updated."})


@app.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    if not MovieModel.get_by_id(movie_id):
        return jsonify({"error": "Movie not found."}), 404
    MovieModel.delete(movie_id)
    return jsonify({"message": "Movie deleted."})


# ── Entry point ──────────────────────────────────────────

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5001)
