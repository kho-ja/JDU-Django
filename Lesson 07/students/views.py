from django.shortcuts import get_object_or_404, redirect, render
from .models import Student
from .forms import StudentSignUpForm


def index(request):
    students = Student.objects.all()
    return render(request, "index.html", context={"students": students})


def view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, "view.html", context={"student": student})


def signup(request):
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students:index")
    else:
        form = StudentSignUpForm()
    return render(request, "students/signup.html", {"form": form})


def edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentSignUpForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students:view", student_id=student.pk)
    else:
        form = StudentSignUpForm(instance=student)
    return render(request, "students/edit.html", {"form": form, "student": student})


def adults(request):
    return render(request, "students/adults.html", {"students": Student.adults.all()})
