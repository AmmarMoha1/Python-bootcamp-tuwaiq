from django.db import models


class Product(models.Model):

    class Category(models.TextChoices):
        LAPTOP = "LAPTOP", "Laptop"
        PHONE = "PHONE", "Phone"
        ACCESSORY = "ACCESSORY", "Accessory"

    name = models.CharField(
        max_length=120,
        db_index=True
    )

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    available_from = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    product_image = models.ImageField(
        upload_to="products/"
    )

    sku = models.CharField(
        max_length=30,
        unique=True
    )

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.ACCESSORY
    )
