from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "student_id",
        "first_name",
        "last_name",
        "email",
        "course",
        "created_at",
    ]
    list_filter = ["course", "created_at"]
    search_fields = ["student_id", "first_name", "last_name", "email"]
    ordering = ["-created_at"]
