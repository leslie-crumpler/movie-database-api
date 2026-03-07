# Movie Database API

A RESTful backend API built with Python (Flask) and SQLite. Demonstrates REST design, filtering, pagination, and proper HTTP status codes.

## Features

- Full CRUD for movies (Create, Read, Update, Delete)
- Filter by genre, year, or rating
- Pagination support (`?page=1&limit=10`)
- Input validation and descriptive error responses
- Clean REST endpoint structure

## Technologies

- Python 3
- Flask
- SQLite

## Project Structure

```
movie-database-api/
├── README.md
├── requirements.txt
├── src/
│   ├── app.py        # Routes and entry point
│   ├── models.py     # Movie data access layer
│   └── database.py   # DB setup
└── tests/
    └── test_api.py
```

## Installation

```bash
git clone https://github.com/lcrumpler/movie-database-api
cd movie-database-api
pip install -r requirements.txt
python src/app.py
```

## API Endpoints

| Method | Endpoint              | Description              |
|--------|-----------------------|--------------------------|
| GET    | /movies               | List movies (filterable) |
| GET    | /movies/\<id\>        | Get single movie         |
| POST   | /movies               | Add a movie              |
| PUT    | /movies/\<id\>        | Update a movie           |
| DELETE | /movies/\<id\>        | Delete a movie           |

## Query Parameters

- `?genre=Action` — filter by genre
- `?year=2020` — filter by release year
- `?page=1&limit=10` — paginate results

## Author

Leslie Crumpler | [GitHub](https://github.com/lcrumpler)
