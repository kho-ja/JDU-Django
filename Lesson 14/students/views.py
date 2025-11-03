from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student


@login_required
def students_page(request):
    """Students page view"""
    if request.method == "POST":
        # Add new student
        student_id = request.POST.get("student_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone", "")
        course = request.POST.get("course")

        # Check if student_id already exists
        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, "Student ID already exists!")
        else:
            Student.objects.create(
                student_id=student_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                course=course,
            )
            messages.success(
                request, f"Student {first_name} {last_name} added successfully!"
            )

        return redirect("students")

    students = Student.objects.all()
    context = {"students": students}
    return render(request, "students.html", context)
