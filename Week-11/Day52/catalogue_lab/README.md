# Catalogue Summary Report

A simple Django project created to practice Django ORM queries and aggregation.

## Features

- Filter active products.
- Group products by category.
- Count products in each category.
- Calculate average product price.
- Calculate total stock.
- Show categories with at least 3 active products.
- Order categories by product count.
- Create an overall summary using `aggregate()`.

## Main Django ORM Methods

- `filter()`
- `values()`
- `annotate()`
- `aggregate()`
- `Count()`
- `Avg()`
- `Sum()`
- `order_by()`

## Run the Project

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell