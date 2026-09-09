# Product Explorer

A simple Django Product Explorer project that demonstrates path parameters, query parameters, filtering, searching, sorting, pagination, tabs, and safe validation.

Users can search for products using `q`, filter by category and minimum price, and sort products by name, price, or rating. The project also preserves active query parameters when navigating between pagination pages.

Each product has a dynamic detail page using its ID. The detail page supports `details`, `reviews`, and `shipping` tabs using the `tab` query parameter. Invalid product IDs return a 404 page, and invalid query parameter values are handled safely.

## Screenshots

### Product List
![Home Page](screenshots/home-page.png)

### Search, Filter and Sort
![Filter Page](screenshots/filter-page.png)

### Pagination
![Pagination Page](screenshots/pagination-page.png)

### Product Detail Tab
![Tab Page](screenshots/tab-page.png)

### Invalid Product ID
![404 Page](screenshots/404-page.png)

## Run the Project

```bash
python manage.py runserver