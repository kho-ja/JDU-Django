from django.contrib import admin
from .models import Course, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "email")
    search_fields = ("name", "email")
    list_filter = ("age",)
