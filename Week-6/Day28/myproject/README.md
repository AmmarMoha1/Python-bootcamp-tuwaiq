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



