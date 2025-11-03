from django.db import models


class Application(models.Model):
    """
    Model to store uploaded applications with title, description, and file.
    """

    title = models.CharField(max_length=200, verbose_name="Nomi")
    description = models.TextField(blank=True, verbose_name="Ta'rifi")
    file = models.FileField(upload_to="applications/", verbose_name="Fayli")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
