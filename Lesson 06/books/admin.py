from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'release_date')
    search_fields = ('name', 'author', 'release_date')

admin.site.register(Book, BookAdmin)
