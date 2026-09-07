from django.shortcuts import render


def home(request):
    context = {
        "title": "Home",
        "username": "Ammar",
    }

    return render(request, "home.html", context)


def courses(request):
    courses_list = [
        {
            "title": "Python Basics",
            "description": "Learn the basics of Python programming.",
            "available": True,
        },
        {
            "title": "Django Basics",
            "description": "Learn how to build web applications with Django.",
            "available": True,
        },
        {
            "title": "Advanced Django",
            "description": "Learn advanced Django concepts.",
            "available": False,
        },
    ]

    context = {
        "title": "Courses",
        "courses": courses_list,
    }

    return render(request, "courses.html", context)


def about(request):
    context = {
        "title": "About",
        "description": "A simple Django learning platform.",
    }

    return render(request, "about.html", context)
