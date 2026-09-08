from django.urls import path

from . import views


app_name = "profiles"


urlpatterns = [
    path(
        "",
        views.upload_profile,
        name="profile",
    ),
    path(
        "profile/",
        views.upload_profile,
        name="profile_page",
    ),
]
