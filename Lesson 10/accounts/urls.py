from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path("logout/", views.logout_view, name="logout"),
    path("static-demo/", views.static_demo_view, name="static_demo"),
    path("", views.static_demo_view, name="home"),  # Home page
]
