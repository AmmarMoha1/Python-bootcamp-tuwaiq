from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View


class RegisterView(View):

    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.POST.get("username")

        if not username:
            return render(
                request,
                "register.html",
                {"error": "Username is required"},
            )

        # Save registered username in session
        request.session["registered_username"] = username

        return redirect("accounts:login")


class LoginView(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")

        # Get registered username from session
        registered_username = request.session.get(
            "registered_username"
        )

        if not registered_username:
            return render(
                request,
                "login.html",
                {"error": "Please register first"},
            )

        if username == registered_username:
            request.session["logged_in"] = True
            request.session["username"] = username

            return redirect("accounts:profile")

        return render(
            request,
            "login.html",
            {"error": "Invalid username"},
        )


class ProfileView(View):

    def get(self, request):
        logged_in = request.session.get("logged_in")

        if not logged_in:
            return redirect("accounts:login")

        username = request.session.get("username")

        return render(
            request,
            "profile.html",
            {"username": username},
        )


def status(request):
    return JsonResponse({
        "status": "success",
        "method": request.method,
    })
