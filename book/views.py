from django.shortcuts import render
from .models import Book


def index(request):
    book = Book.objects.all()
    context = {'book': book}
    return render(request, 'book/index.html', context)


def read(request, slug):
    book = Book.objects.get(slug=slug)
    context = {'book': book}
    return render(request, 'book/read.html', context)

