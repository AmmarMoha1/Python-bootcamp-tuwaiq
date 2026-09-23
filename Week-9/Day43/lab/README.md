# Week 9 - Django Online Store Models

## Overview

This project was created to practice Django model relationships by modeling a simple online store.

The project includes models for categories, products, customer profiles, orders, and order items.

## Models

### Category

A category can optionally have another category as its parent.

This creates a self-referencing relationship.

```python
parent = models.ForeignKey(
    "self",
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="children",
)
```

### Product

Each product belongs to one category.

The Product model also includes:

* SKU
* Name
* Description
* Category
* Price
* Stock
* Active status
* Created date
* Updated date

### CustomerProfile

Each Django User has one CustomerProfile using a `OneToOneField`.

### Order

Each order belongs to one User.

An order can contain many products.

### OrderItem

`OrderItem` connects an `Order` with a `Product`.

It stores:

* Quantity
* Unit price

The `Order` and `Product` models therefore have a many-to-many relationship through `OrderItem`.

## Relationships

```text
Category
   |
   | self ForeignKey
   v
Category


Category
   ^
   |
   | ForeignKey
   |
Product


User
   |
   | OneToOne
   v
CustomerProfile


User
   ^
   |
   | ForeignKey
   |
Order


Order
   |
   v
OrderItem
   |
   v
Product
```

## on_delete Choices

### Category Parent - SET_NULL

`SET_NULL` keeps the child category when its parent category is deleted.

### Product Category - PROTECT

`PROTECT` prevents deleting a category while products still belong to it.

### CustomerProfile User - CASCADE

`CASCADE` deletes the customer profile when its user is deleted.

### Order User - PROTECT

`PROTECT` prevents deleting a user who still has orders and helps preserve order history.

### OrderItem Order - CASCADE

`CASCADE` removes the order items when their order is deleted.

### OrderItem Product - PROTECT

`PROTECT` prevents deleting a product that is referenced by an existing order item.

## Why Quantity Is Stored in OrderItem

Quantity belongs in `OrderItem` because it describes how many units of a specific product are included in a specific order.

For example:

```text
Order 1
- iPhone: quantity = 2
- Charger: quantity = 3

Order 2
- iPhone: quantity = 1
```

The quantity cannot belong directly to `Product` because the same product can have a different quantity in each order.

It also cannot belong directly to `Order` because one order can contain multiple products with different quantities.

## Project Check

Run:

```bash
python manage.py check
```

Expected output:

```text
System check identified no issues (0 silenced).
```

## Note

This lab focuses only on defining Django models and relationships.

Migrations are not run yet.
