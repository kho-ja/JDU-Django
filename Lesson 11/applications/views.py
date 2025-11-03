from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Application
from .forms import ApplicationForm


def application_list(request):
    """
    View to display all uploaded applications and handle new uploads.
    """
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Application muvaffaqiyatli yuklandi!")
            return redirect("application_list")
    else:
        form = ApplicationForm()

    applications = Application.objects.all()

    context = {
        "form": form,
        "applications": applications,
    }
    return render(request, "applications/index.html", context)
