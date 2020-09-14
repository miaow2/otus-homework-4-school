from django.contrib.auth.models import User
from django.db import models


class Professor(User):
    type = models.CharField(
        max_length=30,
        default='professor'
    )
    courses = models.ManyToManyField(
        to='courses.Course',
        blank=True,
        related_name='professors'
    )


class Student(User):
    type = models.CharField(
        max_length=30,
        default='student'
    )
    courses = models.ManyToManyField(
        to='courses.Course',
        blank=True,
        related_name='students'
    )
