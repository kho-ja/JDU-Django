from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Student


@login_required
def students_page(request):
    """Students page view with CRUD operations and search"""

    # Get all students
    students = Student.objects.all()

    # Search functionality by guruh and jdu_id
    search_query = request.GET.get("search", "")
    if search_query:
        students = students.filter(
            Q(jdu_id__icontains=search_query)
            | Q(guruh__icontains=search_query)
            | Q(first_name__icontains=search_query)
            | Q(last_name__icontains=search_query)
        )

    # Handle POST requests for CREATE operation
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "add":
            # Add new student
            jdu_id = request.POST.get("jdu_id")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            phone = request.POST.get("phone", "")
            guruh = request.POST.get("guruh", "")
            course = request.POST.get("course", 1)

            # Check if jdu_id already exists
            if Student.objects.filter(jdu_id=jdu_id).exists():
                messages.error(request, "JDU ID already exists!")
            elif Student.objects.filter(email=email).exists():
                messages.error(request, "Email already exists!")
            else:
                Student.objects.create(
                    jdu_id=jdu_id,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    guruh=guruh,
                    course=course,
                )
                messages.success(
                    request, f"Student {first_name} {last_name} added successfully!"
                )

        elif action == "update":
            # Update existing student
            student_id = request.POST.get("student_id")
            student = get_object_or_404(Student, id=student_id)

            student.first_name = request.POST.get("first_name", student.first_name)
            student.last_name = request.POST.get("last_name", student.last_name)
            student.email = request.POST.get("email", student.email)
            student.phone = request.POST.get("phone", student.phone)
            student.guruh = request.POST.get("guruh", student.guruh)
            student.course = request.POST.get("course", student.course)
            student.save()

            messages.success(
                request, f"Student {student.get_full_name()} updated successfully!"
            )

        return redirect("students")

    context = {
        "students": students,
        "search_query": search_query,
        "total_students": Student.objects.count(),
    }
    return render(request, "students.html", context)


@login_required
def delete_student(request, student_id):
    """Delete student view"""
    student = get_object_or_404(Student, id=student_id)
    student_name = student.get_full_name()
    student.delete()
    messages.success(request, f"Student {student_name} deleted successfully!")
    return redirect("students")
