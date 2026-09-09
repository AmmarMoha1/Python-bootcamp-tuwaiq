from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render


PRODUCTS = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "electronics",
        "price": 3500,
        "rating": 4.8,
        "description": "Powerful laptop for work and study.",
    },
    {
        "id": 2,
        "name": "Headphones",
        "category": "electronics",
        "price": 450,
        "rating": 4.5,
        "description": "Wireless headphones with clear sound.",
    },
    {
        "id": 3,
        "name": "Running Shoes",
        "category": "sports",
        "price": 300,
        "rating": 4.2,
        "description": "Comfortable shoes for running.",
    },
    {
        "id": 4,
        "name": "Football",
        "category": "sports",
        "price": 120,
        "rating": 4.6,
        "description": "High quality football.",
    },
    {
        "id": 5,
        "name": "Backpack",
        "category": "accessories",
        "price": 200,
        "rating": 4.1,
        "description": "Simple backpack for daily use.",
    },
    {
        "id": 6,
        "name": "Smart Watch",
        "category": "electronics",
        "price": 900,
        "rating": 4.7,
        "description": "Smart watch with fitness tracking.",
    },
]


def product_list(request):
    products = PRODUCTS.copy()

    category = request.GET.get("category", "").strip()
    search_query = request.GET.get("q", "").strip()
    min_price = request.GET.get("min_price", "").strip()
    sort = request.GET.get("sort", "name")

    # Category filter
    if category:
        products = [
            product
            for product in products
            if product["category"] == category
        ]

    # Search
    if search_query:
        products = [
            product
            for product in products
            if search_query.lower()
            in product["name"].lower()
        ]

    # Minimum price filter
    if min_price:
        try:
            min_price_value = float(min_price)

            products = [
                product
                for product in products
                if product["price"] >= min_price_value
            ]

        except ValueError:
            min_price = ""

    # Safe sorting
    allowed_sorts = [
        "name",
        "price",
        "rating",
    ]

    if sort not in allowed_sorts:
        sort = "name"

    products = sorted(
        products,
        key=lambda product: product[sort],
    )

    # Pagination
    paginator = Paginator(
        products,
        2,
    )

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(
        page_number
    )

    # Preserve query parameters
    query_params = request.GET.copy()

    if "page" in query_params:
        del query_params["page"]

    context = {
        "page_obj": page_obj,
        "category": category,
        "search_query": search_query,
        "min_price": min_price,
        "sort": sort,
        "query_string": query_params.urlencode(),
    }

    return render(
        request,
        "product_list.html",
        context,
    )


def product_detail(request, id):
    product = None

    for item in PRODUCTS:
        if item["id"] == id:
            product = item
            break

    if product is None:
        raise Http404("Product not found")

    tab = request.GET.get(
        "tab",
        "details",
    )

    allowed_tabs = [
        "details",
        "reviews",
        "shipping",
    ]

    if tab not in allowed_tabs:
        tab = "details"

    context = {
        "product": product,
        "tab": tab,
    }

    return render(
        request,
        "product_detail.html",
        context,
    )
