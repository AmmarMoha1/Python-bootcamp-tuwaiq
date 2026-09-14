from django.urls import path

from . import views


app_name = "store"


urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "set-theme/<str:theme>/",
        views.set_theme,
        name="set_theme",
    ),

    path(
        "add/<int:product_id>/",
        views.add_to_cart,
        name="add_to_cart",
    ),

    path(
        "clear-cart/",
        views.clear_cart,
        name="clear_cart",
    ),
]
