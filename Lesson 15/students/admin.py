from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "jdu_id",
        "first_name",
        "last_name",
        "email",
        "guruh",
        "course",
        "created_at",
    ]
    list_filter = ["course", "guruh", "created_at"]
    search_fields = ["jdu_id", "first_name", "last_name", "email", "guruh"]
    ordering = ["-created_at"]
