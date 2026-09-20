from django.db import models


class Product(models.Model):

    class Category(models.TextChoices):
        PHONES = "PHONES", "Phones"
        LAPTOPS = "LAPTOPS", "Laptops"
        ACCESSORIES = "ACCESSORIES", "Accessories"

    sku = models.CharField(
        max_length=50,
        unique=True,
    )

    name = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
    )

    category = models.CharField(
    max_length=20,
    choices=Category.choices,
    default=Category.PHONES,
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    stock = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
