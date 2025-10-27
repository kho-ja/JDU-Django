from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    """
    Login funksiyasi:
    - GET so'rovi: login formasini ko'rsatadi
    - POST so'rovi: foydalanuvchini autentifikatsiya qiladi
    - To'g'ri login/parol bo'lsa: profile sahifasiga yo'naltiradi
    - Xato bo'lsa: login sahifasiga qaytaradi va xabar ko'rsatadi
    """
    # Agar foydalanuvchi allaqachon tizimga kirgan bo'lsa, profilga yo'naltirish
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Foydalanuvchini autentifikatsiya qilish
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login muvaffaqiyatli
            auth_login(request, user)
            messages.success(
                request,
                f"Xush kelibsiz, {user.username}! Siz tizimga muvaffaqiyatli kirdingiz.",
            )
            return redirect("profile")
        else:
            # Login yoki parol xato
            messages.error(
                request, "Login yoki parol xato! Iltimos, qaytadan urinib ko'ring."
            )
            return redirect("login")

    return render(request, "login.html")


@login_required(login_url="login")
def profile_view(request):
    """
    Profil sahifasi:
    - Faqat tizimga kirgan foydalanuvchilar uchun
    - Foydalanuvchi ma'lumotlarini ko'rsatadi
    """
    return render(request, "profile.html")


def logout_view(request):
    """
    Logout funksiyasi:
    - Foydalanuvchini tizimdan chiqaradi
    - Login sahifasiga yo'naltiradi
    - "Siz tizimdan chiqib ketdingiz" xabarini ko'rsatadi
    """
    if request.user.is_authenticated:
        username = request.user.username
        auth_logout(request)
        messages.info(
            request,
            f"{username}, siz tizimdan chiqib ketdingiz. Qaytib kelganingizdan xursandmiz!",
        )

    return redirect("login")
