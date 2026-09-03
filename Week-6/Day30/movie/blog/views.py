from django.http import Http404
from django.shortcuts import render


posts = [
    {
        "id": 1,
        "title": "Learning Django",
        "category": "django",
    },
    {
        "id": 2,
        "title": "Python Basics",
        "category": "python",
    },
    {
        "id": 3,
        "title": "Django Routing",
        "category": "django",
    },
]


def post_list(request):
    return render(
        request,
        "blog/post_list.html",
        {"posts": posts},
    )


def post_detail(request, post_id):
    post = None

    for item in posts:
        if item["id"] == post_id:
            post = item
            break

    if post is None:
        raise Http404("Post not found")

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )


def category_posts(request, category):
    filtered_posts = []

    for post in posts:
        if post["category"] == category:
            filtered_posts.append(post)

    return render(
        request,
        "blog/category.html",
        {
            "posts": filtered_posts,
            "category": category,
        },
    )
