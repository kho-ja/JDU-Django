from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        "Author",
        related_name="books",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
