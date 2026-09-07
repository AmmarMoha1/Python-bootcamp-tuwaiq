from django.shortcuts import render


courses_data = [
    {
        "id": 1,
        "name": "python basics",
        "level": "beginner",
        "student_count": 25,
        "description": (
            "Learn Python programming from the beginning "
            "and understand variables, conditions, loops, "
            "functions, and basic programming concepts."
        ),
        "image": "python.jpg",
    },
    {
        "id": 2,
        "name": "django web development",
        "level": "intermediate",
        "student_count": 15,
        "description": (
            "<strong>Build web applications</strong> "
            "using Django, templates, views, URLs, "
            "and reusable components."
        ),
        "image": "django.jpg",
    },
    {
        "id": 3,
        "name": "react fundamentals",
        "level": "beginner",
        "student_count": 0,
        "description": (
            "Learn the fundamentals of React and "
            "how to create reusable user interface components."
        ),
        "image": "react.jpg",
    },
]


def home(request):
    context = {
        "username": "Ammar",
    }

    return render(
        request,
        "home.html",
        context,
    )


def course_list(request):
    context = {
        "username": "Ammar",
        "courses": courses_data,
    }

    return render(
        request,
        "courses.html",
        context,
    )


def course_detail(request, course_id):
    course = None

    for item in courses_data:
        if item["id"] == course_id:
            course = item
            break

    context = {
        "course": course,
    }

    return render(
        request,
        "course_detail.html",
        context,
    )
