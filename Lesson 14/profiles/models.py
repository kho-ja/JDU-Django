from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """User Profile model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, verbose_name="Bio")
    avatar = models.ImageField(
        upload_to="avatars/", blank=True, null=True, verbose_name="Avatar"
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    address = models.TextField(blank=True, verbose_name="Manzil")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Tug'ilgan sana")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan")

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profillar"

    def __str__(self):
        return f"{self.user.username}'s profile"
