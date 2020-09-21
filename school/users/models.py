from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    professor = models.BooleanField(default=False)
    student = models.BooleanField(default=False)

    @property
    def is_professor(self):
        return self.professor

    @property
    def is_student(self):
        return self.student
