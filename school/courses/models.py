from django.db import models
from django.urls.base import reverse


CATEGORIES = (
    ("network", "Network"),
    ("linux", "Linux"),
    ("devops", "DevOps"),
    ("programming", "Programming"),
)


class Course(models.Model):
    name = models.CharField(
        max_length=30
    )
    category = models.CharField(
        max_length=50, choices=CATEGORIES,
    )
    duration = models.PositiveIntegerField(
        help_text="Duration in days"
    )
    description = models.TextField()
    participants = models.ManyToManyField(
        to='users.User',
        blank=True,
        related_name="courses"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:course', args=[self.pk])

    @property
    def text_short(self):
        if len(self.description) < 40:
            return self.description
        return f'{self.description[:40]}...'

    @property
    def students(self):
        return self.participants.filter(student=True)

    @property
    def professors(self):
        return self.participants.filter(professor=True)


class Lesson(models.Model):
    name = models.CharField(
        max_length=30
    )
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        related_name="lessons"
    )
    duration = models.PositiveIntegerField(
        help_text="Duration in minutes"
    )
    description = models.TextField()

    class Meta:
        unique_together = [
            ['course', 'name']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:lesson', args=[self.pk])

    @property
    def text_short(self):
        if len(self.description) < 40:
            return self.description
        return f'{self.description[:40]}...'
