from django.db.models import Avg, Count, Sum

from .models import Product


def category_report():
    return (
        Product.objects
        .filter(is_active=True)
        .values(
            "category_id",
            "category__name",
        )
        .annotate(
            product_count=Count("id"),
            average_price=Avg("price"),
            total_stock=Sum("stock"),
        )
        .filter(product_count__gte=3)
        .order_by(
            "-product_count",
            "category__name",
        )
    )


def overall_summary():
    return (
        Product.objects
        .filter(is_active=True)
        .aggregate(
            total_products=Count("id"),
            average_price=Avg("price"),
        )
    )

