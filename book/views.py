from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    book = Book.objects.all()
    context = {'book': book}
    return render(request, 'book/index.html', context)
