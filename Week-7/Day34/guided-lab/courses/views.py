from django.shortcuts import render


COURSES = [
    {
        "id": 1,
        "title": "Python Basics",
        "category": "programming",
        "difficulty": "beginner",
        "description": "Learn Python from the beginning.",
        "syllabus": "Variables, conditions, loops, functions.",
        "instructor": "Ahmed",
    },
    {
        "id": 2,
        "title": "Django Development",
        "category": "programming",
        "difficulty": "intermediate",
        "description": "Build web applications using Django.",
        "syllabus": "URLs, views, templates, models.",
        "instructor": "Mohammed",
    },
    {
        "id": 3,
        "title": "UI UX Basics",
        "category": "design",
        "difficulty": "beginner",
        "description": "Learn the basics of UI and UX design.",
        "syllabus": "Research, wireframes, prototypes.",
        "instructor": "Sara",
    },
    {
        "id": 4,
        "title": "Advanced Python",
        "category": "programming",
        "difficulty": "advanced",
        "description": "Learn advanced Python concepts.",
        "syllabus": "OOP, decorators, generators.",
        "instructor": "Ali",
    },
    {
        "id": 5,
        "title": "Graphic Design",
        "category": "design",
        "difficulty": "intermediate",
        "description": "Introduction to graphic design.",
        "syllabus": "Colors, typography, composition.",
        "instructor": "Nora",
    },
]


def course_list(request):
    category = request.GET.get("category", "")
    difficulty = request.GET.get("difficulty", "")
    search_query = request.GET.get("q", "")

    filtered_courses = COURSES

    if category:
        filtered_courses = [
            course
            for course in filtered_courses
            if course["category"] == category
        ]

    if difficulty:
        filtered_courses = [
            course
            for course in filtered_courses
            if course["difficulty"] == difficulty
        ]

    if search_query:
        filtered_courses = [
            course
            for course in filtered_courses
            if search_query.lower() in course["title"].lower()
        ]

    # Pagination
    page = request.GET.get("page", "1")

    try:
        page = int(page)
    except ValueError:
        page = 1

    if page < 1:
        page = 1

    per_page = 2

    start = (page - 1) * per_page
    end = start + per_page

    paginated_courses = filtered_courses[start:end]

    total_pages = (
        len(filtered_courses) + per_page - 1
    ) // per_page

    context = {
        "courses": paginated_courses,
        "category": category,
        "difficulty": difficulty,
        "search_query": search_query,
        "page": page,
        "total_pages": total_pages,
    }

    return render(
        request,
        "course_list.html",
        context,
    )


def course_detail(request, course_id):
    course = None

    for item in COURSES:
        if item["id"] == course_id:
            course = item
            break

    tab = request.GET.get(
        "tab",
        "details",
    )

    allowed_tabs = [
        "details",
        "syllabus",
        "instructor",
    ]

    if tab not in allowed_tabs:
        tab = "details"

    context = {
        "course": course,
        "tab": tab,
    }

    return render(
        request,
        "course_detail.html",
        context,
    )
