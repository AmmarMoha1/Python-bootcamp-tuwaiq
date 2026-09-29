from django.db.models import Q

from .models import Product


def search_products(
    search=None,
    min_price=None,
    max_price=None,
    category_name=None,
):
    # 1 - Start with active Product records
    queryset = Product.objects.filter(
        is_active=True
    )

    # 2 - Keep products whose stock is above zero
    queryset = queryset.filter(
        stock__gt=0
    )

    # 3 - Search name OR SKU with a Q object
    if search:
        queryset = queryset.filter(
            Q(name__icontains=search)
            | Q(sku__icontains=search)
        )

    # 4 - Apply optional minimum price
    if min_price is not None:
        queryset = queryset.filter(
            price__gte=min_price
        )

    # 4 - Apply optional maximum price
    if max_price is not None:
        queryset = queryset.filter(
            price__lte=max_price
        )

    # 5 - Filter by category name
    # across the relationship
    if category_name:
        queryset = queryset.filter(
            category__name__iexact=category_name
        )

    # 6 - Order by price, then name, then pk
    queryset = queryset.order_by(
        "price",
        "name",
        "pk",
    )

    # 7 - Return the first 10 results
    first_10 = queryset[:10]

    # 8 - Produce a values() result
    # with name, SKU, and price
    product_values = queryset.values(
        "name",
        "sku",
        "price",
    )[:10]

    return first_10, product_values
