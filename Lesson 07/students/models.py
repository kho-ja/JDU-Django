from django.db import models


class AdultsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(age__gte=18)


class Course(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name="students", blank=True)

    objects = models.Manager()
    adults = AdultsManager()

    def __str__(self):
        return self.name
