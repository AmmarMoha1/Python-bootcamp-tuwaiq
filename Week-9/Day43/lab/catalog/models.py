from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100,
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    def __str__(self):
        return self.name


class Product(models.Model):
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

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
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


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="customer_profile",
    )

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="orders",
    )

    products = models.ManyToManyField(
        Product,
        through="OrderItem",
        related_name="orders",
    )

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="order_items",
    )

    quantity = models.PositiveIntegerField()

    unit_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
