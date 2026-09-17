from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    available_from = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    product_image = models.ImageField(
        upload_to="products/"
    )
