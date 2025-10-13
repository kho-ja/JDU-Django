from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=100, null=True)
    published_date = models.DateField(null=True)