from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_date = models.DateField(null=True)

    def __str__(self):
        return self.name