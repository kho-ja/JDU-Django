from django.db import models

class Maktab(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    established_date = models.DateField(null=True, blank=True)
    principal = models.CharField(max_length=100, null=True, blank=True)
    student_count = models.IntegerField(null=True, blank=True)