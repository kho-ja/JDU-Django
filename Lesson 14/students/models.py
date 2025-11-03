from django.db import models


class Student(models.Model):
    """Student model"""

    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, verbose_name="Familiya")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    student_id = models.CharField(max_length=20, unique=True, verbose_name="Talaba ID")
    course = models.IntegerField(default=1, verbose_name="Kurs")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan")

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

    def get_full_name(self):
        """Return full name"""
        return f"{self.first_name} {self.last_name}"
