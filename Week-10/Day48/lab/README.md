# Product Search Lab

A simple Django project that demonstrates how to build and refine Django QuerySets using filters, `Q` objects, relationships, ordering, slicing, and `values()`.

## Project Features

This lab demonstrates how to:

- Retrieve active products.
- Filter products with stock greater than zero.
- Search products by name or SKU using a `Q` object.
- Apply optional minimum and maximum price filters.
- Filter products by category name through a relationship.
- Order products by price, name, and primary key.
- Return only the first 10 results.
- Use `values()` to return selected fields.
- Understand Django QuerySet lazy evaluation.

## Technologies Used

- Python
- Django
- SQLite

## Project Structure

```text
product_search_lab/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── queries.py
│   ├── tests.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

## Models

The project contains two models:

### Category

Represents a product category.

```python
class Category(models.Model):
    name = models.CharField(max_length=100)
```

### Product

Represents a product with its name, SKU, price, stock, active status, and category.

```python
class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
    )
```

## Installation

Clone or download the project, then open the project directory.

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install Django:

```bash
pip install django
```

Create the database migrations:

```bash
python manage.py makemigrations
```

Apply the migrations:

```bash
python manage.py migrate
```

## QuerySet Implementation

The main QuerySet logic is located in:

```text
store/queries.py
```

The function accepts optional search parameters:

```python
search_products(
    search=None,
    min_price=None,
    max_price=None,
    category_name=None,
)
```

### Active Products

Only active products are included:

```python
queryset = Product.objects.filter(
    is_active=True
)
```

### Stock Filter

Products must have stock greater than zero:

```python
queryset = queryset.filter(
    stock__gt=0
)
```

### Search by Name or SKU

A Django `Q` object is used to search either the product name or SKU:

```python
if search:
    queryset = queryset.filter(
        Q(name__icontains=search)
        | Q(sku__icontains=search)
    )
```

### Price Filters

Minimum price:

```python
if min_price is not None:
    queryset = queryset.filter(
        price__gte=min_price
    )
```

Maximum price:

```python
if max_price is not None:
    queryset = queryset.filter(
        price__lte=max_price
    )
```

### Category Filter

Products can be filtered through the `Category` relationship:

```python
if category_name:
    queryset = queryset.filter(
        category__name__iexact=category_name
    )
```

### Ordering

Products are ordered by:

1. Price
2. Name
3. Primary key

```python
queryset = queryset.order_by(
    "price",
    "name",
    "pk",
)
```

### First 10 Results

Only the first 10 results are returned:

```python
first_10 = queryset[:10]
```

### Using `values()`

The second result contains only the product name, SKU, and price:

```python
product_values = queryset.values(
    "name",
    "sku",
    "price",
)[:10]
```

## Testing the Query

Open the Django shell:

```bash
python manage.py shell
```

Import the search function:

```python
from store.queries import search_products
```

Example:

```python
products, values = search_products(
    search="iphone",
    min_price=1000,
    max_price=5000,
    category_name="Electronics",
)
```

View the products:

```python
list(products)
```

View the selected values:

```python
list(values)
```

Example output:

```python
[
    {
        "name": "iPhone 17",
        "sku": "IPH17",
        "price": Decimal("3999.00"),
    }
]
```

## QuerySet Lazy Evaluation

Django QuerySets use lazy evaluation.

Operations such as:

```python
filter()
order_by()
values()
[:10]
```

refine or build the QuerySet but normally do not immediately execute the SQL query.

The QuerySet is evaluated when the data is actually required.

Examples:

```python
list(queryset)
```

or:

```python
for product in queryset:
    print(product.name)
```

At this point, Django executes the database query.

## Learning Outcomes

After completing this lab, I learned how to:

- Create Django models and relationships.
- Work with Django QuerySets.
- Use field lookups such as `gt`, `gte`, `lte`, `icontains`, and `iexact`.
- Combine search conditions using Django `Q` objects.
- Filter across a ForeignKey relationship.
- Sort QuerySet results.
- Limit QuerySet results using slicing.
- Retrieve selected fields using `values()`.
- Understand lazy evaluation in Django QuerySets.