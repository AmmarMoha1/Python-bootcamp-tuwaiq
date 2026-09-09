from django.urls import path

from . import views


app_name = "products"


urlpatterns = [
    path(
        "products/",
        views.product_list,
        name="list",
    ),

    path(
        "products/<int:id>/",
        views.product_detail,
        name="detail",
    ),
]
