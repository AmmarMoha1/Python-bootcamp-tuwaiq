# Week 9 - Django Product Model

## Overview

This project was created to practice Django Models and model fields.

The project contains a `Product` model inside the `catalog` app.

## Product Fields

The `Product` model includes:

* SKU
* Name
* Description
* Category
* Price
* Stock
* Active status
* Created date
* Updated date

## Categories

The available product categories are:

* Phones
* Laptops
* Accessories

## Concepts Used

* Django Models
* `CharField`
* `TextField`
* `DecimalField`
* `PositiveIntegerField`
* `BooleanField`
* `DateTimeField`
* `TextChoices`
* `unique=True`
* `blank=True`
* `default`
* `__str__()`

## Run the Project Check

```bash
python manage.py check
```

If everything is correct:

```text
System check identified no issues (0 silenced).
```
