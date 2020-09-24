import factory

from .models import Course, Lesson


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course


class LessonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lesson
