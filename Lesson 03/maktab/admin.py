from django.contrib import admin
from .models import Maktab

class MaktabAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'established_date', 'principal', 'student_count')
    search_fields = ('name', 'location', 'principal')

admin.site.register(Maktab, MaktabAdmin)