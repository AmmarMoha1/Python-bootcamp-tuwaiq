from django.shortcuts import render


def course_list(request):
    return render(request, "courses_list.html")


def course_detail(request, slug):
    return render(
        request,
        "course_detail.html",
        {"slug": slug},
    )


def course_category(request, category):
    return render(
        request,
        "course_category.html",
        {"category": category},
    )
