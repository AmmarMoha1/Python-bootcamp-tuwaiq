# Week 11 - Django ORM CRUD Lab

## Project Overview

This project demonstrates the basic CRUD operations using the Django ORM.

The lab focuses on working with a `Product` model and performing database operations such as:

- Creating products
- Retrieving products
- Filtering data
- Searching records
- Updating products
- Deleting products
- Using `F()` expressions
- Using QuerySet methods such as `filter()`, `exclude()`, `get()`, `count()`, and `exists()`

---

## Technologies Used

- Python
- Django
- SQLite
- Django ORM

---

## Product Model

The project uses the following `Product` model:

```python
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.IntegerField()

    category = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name
```

The model contains:

- `name` - product name
- `price` - product price
- `stock` - available quantity
- `category` - product category
- `is_active` - product status
- `id` - automatically generated primary key

---

## Database Setup

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

---

## Django Shell

The CRUD operations were tested using the Django shell.

```bash
python manage.py shell
```

Import the Product model:

```python
from catalog.models import Product
```

---

# CRUD Operations

## 1. Create Products

Three products were created with different prices, stock values, and categories.

```python
p1 = Product.objects.create(
    name="Mechanical Keyboard",
    price=349.00,
    stock=12,
    category="Accessories",
    is_active=True
)

p2 = Product.objects.create(
    name="USB Hub",
    price=89.00,
    stock=0,
    category="Accessories",
    is_active=True
)

p3 = Product.objects.create(
    name="Gaming Mouse",
    price=199.00,
    stock=5,
    category="Peripherals",
    is_active=True
)
```

`objects.create()` creates and saves the object directly to the database.

---

## 2. Retrieve All Products

```python
products = Product.objects.all()
```

Display the primary key and name:

```python
for product in products:
    print(product.pk, product.name)
```

`pk` represents the primary key of each product.

---

## 3. Filter Active Products With Available Stock

```python
active_products = Product.objects.filter(
    is_active=True,
    stock__gt=0
)
```

Display the results:

```python
for product in active_products:
    print(product.name, product.stock)
```

`stock__gt=0` means:

```text
stock > 0
```

---

## 4. Search by Product Name

```python
search_term = "key"

results = Product.objects.filter(
    name__icontains=search_term
)
```

Display the results:

```python
for product in results:
    print(product.name)
```

`icontains` performs a case-insensitive search.

---

## 5. Retrieve One Product

A single product can be retrieved using its primary key.

```python
product = Product.objects.get(pk=1)
```

A missing product can be handled using `try` and `except`.

```python
try:
    product = Product.objects.get(pk=9999)
    print(product.name)

except Product.DoesNotExist:
    print("Product not found")
```

`get()` expects exactly one object.

---

## 6. Update One Product

Retrieve the product:

```python
product = Product.objects.get(name="Gaming Mouse")
```

Update its values:

```python
product.price = 179.00
product.stock = 8
```

Save only the modified fields:

```python
product.save(
    update_fields=["price", "stock"]
)
```

Changing model attributes alone does not update the database until `save()` is called.

---

## 7. Update Multiple Products

All products in the `Accessories` category were deactivated:

```python
changed = Product.objects.filter(
    category="Accessories"
).update(
    is_active=False
)
```

Display the number of updated rows:

```python
print(changed)
```

`update()` performs the database update directly on all matching rows.

---

## 8. Delete Products

Inactive products with zero stock were deleted:

```python
deleted = Product.objects.filter(
    is_active=False,
    stock=0
).delete()
```

This removes only products that satisfy both conditions.

---

# F Expressions

Django `F()` expressions allow database fields to be updated using their current values.

Import `F`:

```python
from django.db.models import F
```

Decrease stock by one:

```python
Product.objects.filter(
    name="Gaming Mouse"
).update(
    stock=F("stock") - 1
)
```

`F("stock")` represents the current value of the `stock` field in the database.

---

# QuerySet Methods

## `all()`

Returns all records:

```python
Product.objects.all()
```

---

## `filter()`

Returns zero or more matching objects:

```python
Product.objects.filter(
    is_active=True
)
```

---

## `get()`

Returns exactly one object:

```python
Product.objects.get(pk=1)
```

---

## `exclude()`

Excludes records matching a condition:

```python
Product.objects.exclude(
    category="Accessories"
)
```

---

## `first()`

Returns the first matching object or `None`:

```python
Product.objects.filter(
    stock__gt=0
).first()
```

---

## `exists()`

Checks whether any matching record exists:

```python
Product.objects.filter(
    stock=0
).exists()
```

Returns:

```text
True
```

or:

```text
False
```

---

## `count()`

Returns the number of matching rows:

```python
Product.objects.filter(
    is_active=True
).count()
```

---

# QuerySet Chaining

Multiple QuerySet operations can be combined:

```python
products = (
    Product.objects
    .filter(
        is_active=True,
        stock__gt=0
    )
    .exclude(
        category="Clearance"
    )
    .order_by("price")
)
```

This query:

1. Selects active products
2. Requires stock greater than zero
3. Excludes the `Clearance` category
4. Orders the result by price

---

# Important ORM Concepts

## Manager

```python
Product.objects
```

`objects` is the model manager used to start database queries.

---

## QuerySet

Methods such as:

```python
Product.objects.filter(...)
```

return a QuerySet.

A QuerySet can contain zero, one, or many records.

---

## Model Instance

```python
Product.objects.get(pk=1)
```

returns one `Product` instance.

---

## Lazy QuerySets

Django QuerySets are generally lazy.

For example:

```python
products = Product.objects.filter(
    is_active=True
)
```

The database query is usually not executed until the results are actually needed.

For example:

```python
for product in products:
    print(product.name)
```

---

# CRUD Summary

```text
CREATE
Product.objects.create()

READ
Product.objects.all()
Product.objects.filter()
Product.objects.get()

UPDATE
product.save()
QuerySet.update()

DELETE
product.delete()
QuerySet.delete()
```

---

## Key Concepts Learned

- Django ORM
- CRUD operations
- Managers
- QuerySets
- Model instances
- Primary keys
- `get()`
- `filter()`
- `exclude()`
- Field lookups
- `save()`
- `update()`
- `delete()`
- `F()` expressions
- Lazy QuerySets
- Exception handling

---

## Conclusion

This lab demonstrates how Django ORM provides a Python-based interface for working with database records without writing SQL directly.

The project covers the complete CRUD cycle:

```text
Create
Read
Update
Delete
```

It also demonstrates how QuerySets, model instances, field lookups, and `F()` expressions can be used to perform common database operations efficiently.