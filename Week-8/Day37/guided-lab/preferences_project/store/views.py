from django.shortcuts import redirect, render


def home(request):
    theme = request.COOKIES.get(
        "theme",
        "light",
    )

    cart = request.session.get(
        "cart",
        [],
    )

    context = {
        "theme": theme,
        "cart": cart,
        "cart_count": len(cart),
    }

    return render(
        request,
        "home.html",
        context,
    )


def set_theme(request, theme):
    allowed_themes = [
        "light",
        "dark",
    ]

    if theme not in allowed_themes:
        theme = "light"

    response = redirect(
        "store:home"
    )

    response.set_cookie(
        "theme",
        theme,
        max_age=60 * 60 * 24 * 30,
    )

    return response


def add_to_cart(request, product_id):
    cart = request.session.get(
        "cart",
        [],
    )

    cart.append(product_id)

    request.session["cart"] = cart

    return redirect(
        "store:home"
    )


def clear_cart(request):
    request.session.pop(
        "cart",
        None,
    )

    return redirect(
        "store:home"
    )
