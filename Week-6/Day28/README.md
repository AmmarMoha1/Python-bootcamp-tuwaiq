
# Guided Lab: Build a Complete MVT Workflow

## Overview

In this lab, we built a simple Django Library application to understand the complete MVT workflow.

Before this lab, we learned about **Context** and how a View can send data to a Template.

In this lab, we connected the following parts together:

Browser → URL → View → Context → Template → Response

---

## Project Structure

The project contains a `library` app with:

- `urls.py` - Defines the URLs for the library pages.
- `views.py` - Contains the logic for displaying the books.
- `templates/` - Contains the HTML templates.
- `base.html` - The main template used by the other pages.
- `book_list.html` - Displays the list of books.
- `book_detail.html` - Displays details about a selected book.

---

## In-Memory Books List

We created a list of books inside `views.py` instead of using a database.

Each book contains:

- ID
- Title
- Author

Example:

```python
books = [
    {
        'id': 1,
        'title': 'Django for Beginners',
        'author': 'Author 1'
    },
    {
        'id': 2,
        'title': 'Python for Beginners',
        'author': 'Author 2'
    },
]
```

# CHALLENGE: Movie Catalog

A simple Django project that displays a list of movies and allows users to view the details of each movie.

## Features

* Display a list of movies
* View movie details
* Use dynamic URLs
* Use named URLs
* Use Django templates
* Template inheritance using `base.html`
* Store movie data in an in-memory Python list

## Movie Data

Each movie contains:

* Title
* Year
* Rating

The movie data is stored in a Python list instead of a database.

## Pages

### Movie List

`/movies/`

Displays all available movies with their title, year, and rating.

### Movie Details

`/movies/<movie_id>/`

Displays the details of a specific movie based on its ID.

Example:

`/movies/2/`

## MVT Flow

This project follows Django's MVT structure:

* **Model / Data:** Movie data is stored in a Python list.
* **View:** The views receive the request, get the required movie data, and send it to the template.
* **Template:** The templates display the movie data as HTML.

The request flow is:

`URL → View → Data → Template → Response`

For example, when the user visits `/movies/`, Django matches the URL with the `movie_list` view. The view sends the movies list to `movie_list.html`, and the template displays the movies to the user.

## Project Structure

```text
movie/
│
├── manage.py
│
├── mysite/
│   ├── settings.py
│   └── urls.py
│
└── movie/
    ├── urls.py
    ├── views.py
    └── templates/
        ├── base.html
        └── movie/
            ├── movie_list.html
            └── movie_detail.html
```

## Run the Project

```bash
python manage.py runserver
```

Then open:

`http://127.0.0.1:8000/movies/`
