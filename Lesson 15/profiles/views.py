from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile


def sign_in(request):
    """Sign in page view (login with username and password validation)"""
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check username and password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("students")  # Redirect to students page
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "login.html")


def sign_up(request):
    """Sign up page view (registration with redirect)"""
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Validation
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, "register.html")

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password1,
        )

        # Create profile
        Profile.objects.create(user=user)

        messages.success(request, "Registration successful! Please login.")
        return redirect("sign_in")  # Redirect to sign_in

    return render(request, "register.html")


def logout_view(request):
    """Logout view with redirect"""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("sign_in")  # Redirect to sign_in


@login_required
def profile_page(request):
    """Profile page view"""
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        # Handle avatar upload
        if "avatar" in request.FILES:
            profile.avatar = request.FILES["avatar"]
            profile.save()
            messages.success(request, "Avatar updated successfully!")
            return redirect("profile")

        # Update user info
        request.user.first_name = request.POST.get("first_name", "")
        request.user.last_name = request.POST.get("last_name", "")
        request.user.email = request.POST.get("email", "")
        request.user.save()

        # Update profile info
        profile.bio = request.POST.get("bio", "")
        profile.phone = request.POST.get("phone", "")
        profile.address = request.POST.get("address", "")
        profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("profile")

    context = {"profile": profile}
    return render(request, "profile.html", context)


def custom_404(request, exception):
    """Custom 404 page view"""
    return render(request, "404.html", status=404)
