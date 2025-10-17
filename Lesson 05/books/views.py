from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Book

def books(request):
    return render(request, 'books/index.html', context={
        'books': Book.objects.all()
    })

def book_detail(request, book_id):
    return render(request, 'books/view.html', context={
        'book': get_object_or_404(Book, pk=book_id)
    })

def redirect_me(request, book_id):
    return redirect(reverse('books:one', kwargs={'book_id':book_id}))