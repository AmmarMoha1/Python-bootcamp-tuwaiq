from django.db import models
from django.db.models import Q


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
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    stock = models.PositiveIntegerField(
        default=0,
    )

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

    def is_available(self):
        return self.is_active and self.stock > 0

    def inventory_value(self):
        return self.price * self.stock

    class Meta:
        ordering = ["category", "name"]

        verbose_name = "product"
        verbose_name_plural = "products"

        indexes = [
            models.Index(
                fields=["category", "is_active"],
                name="product_cat_active_idx",
            ),
        ]

        constraints = [
            models.CheckConstraint(
                condition=Q(price__gte=0),
                name="product_price_non_negative",
            ),
            models.CheckConstraint(
                condition=Q(stock__gte=0),
                name="product_stock_non_negative",
            ),
        ]
