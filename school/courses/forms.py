from django import forms

from .models import Course, Lesson


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'category', 'duration', 'description']


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ['name', 'course', 'duration', 'description']
