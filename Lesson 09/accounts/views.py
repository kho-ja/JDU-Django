from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError


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


def register_view(request):
    """
    Ro'yxatdan o'tish funksiyasi (CSRF himoyasi bilan):
    - GET so'rovi: registratsiya formasini ko'rsatadi
    - POST so'rovi: yangi foydalanuvchi yaratadi
    - CSRF token template'dan olinadi
    - Muvaffaqiyatli bo'lsa: login sahifasiga yo'naltiradi
    """
    # Agar foydalanuvchi allaqachon tizimga kirgan bo'lsa
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        # Formadan ma'lumotlarni olish (CSRF token avtomatik tekshiriladi)
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")

        # Validatsiya
        if not all([username, email, password1, password2]):
            messages.error(request, "Barcha majburiy maydonlarni to'ldiring!")
            return redirect("register")

        if password1 != password2:
            messages.error(request, "Parollar bir xil emas!")
            return redirect("register")

        if len(password1) < 8:
            messages.error(request, "Parol kamida 8 ta belgidan iborat bo'lishi kerak!")
            return redirect("register")

        try:
            # Yangi foydalanuvchi yaratish
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name,
            )

            messages.success(
                request,
                f"Tabriklaymiz, {username}! Ro'yxatdan o'tish muvaffaqiyatli. Endi tizimga kirishingiz mumkin.",
            )
            return redirect("login")

        except IntegrityError:
            messages.error(
                request, "Bu foydalanuvchi nomi allaqachon band! Boshqa nom tanlang."
            )
            return redirect("register")
        except Exception as e:
            messages.error(request, f"Xatolik yuz berdi: {str(e)}")
            return redirect("register")

    return render(request, "register.html")


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
