from django.urls import path
from .views import index, view, signup, edit, adults

app_name = "students"

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path("adults/", adults, name="adults"),
    path("<int:student_id>/", view, name="view"),
    path("<int:student_id>/edit/", edit, name="edit"),
]
