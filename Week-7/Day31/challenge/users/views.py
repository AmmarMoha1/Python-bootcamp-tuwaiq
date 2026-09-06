from django.shortcuts import render

app_name = "users"

def login_view(request):
    return render(request, "login.html")


def profile(request):
    return render(request, "profile.html")
