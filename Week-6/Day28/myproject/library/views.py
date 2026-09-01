from django.shortcuts import render

# Create your views here.
books = [
    {
        'id': 1,
        'title': 'Welcome to Django',
        'author': 'Ammar'
    },
    {
        'id': 2,
        'title': 'Welcome to Python',
        'author': 'Ammar'
    }
]


def book_list(request):
    return render(request, 'library/book_list.html', {'books': books})


def book_detail(request, id):
    selected_book = next((book for book in books if book['id'] == id), None)
    return render(request, 'library/book_detail.html', {'book': selected_book})
