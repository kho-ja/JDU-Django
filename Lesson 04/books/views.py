from django.http import HttpResponse
from django.shortcuts import render
from .models import Book as Books

def books(request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})