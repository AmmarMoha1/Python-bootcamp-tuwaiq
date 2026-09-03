from django.http import Http404
from django.shortcuts import render


movies = [
    {
        "title": "Interstellar",
        "year": 2014,
        "rating": 8.7,
    },
    {
        "title": "Inception",
        "year": 2010,
        "rating": 8.8,
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
    },
]


def movie_list(request):
    return render(
        request,
        "movie/movie_list.html",
        {"movies": movies},
    )


def movie_detail(request, movie_id):
    index = movie_id - 1

    if index < 0 or index >= len(movies):
        raise Http404("Movie not found")

    movie = movies[index]

    return render(
        request,
        "movie/movie_detail.html",
        {"movie": movie},
    )
