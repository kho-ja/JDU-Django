from django.shortcuts import get_object_or_404, render
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', context={'students': students})

def view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'view.html', context={'student': student})