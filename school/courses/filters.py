import django_filters

from .models import Course, Lesson
from users.models import User


class LessonFilterSet(django_filters.FilterSet):
    course_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Course.objects.all(),
        label='Course ID',
    )
    course = django_filters.ModelMultipleChoiceFilter(
        field_name='name',
        queryset=Course.objects.all(),
        to_field_name='name',
        label='Course name',
    )

    class Meta:
        model = Lesson
        fields = ['id', 'name']


class CourseFilterSet(django_filters.FilterSet):
    participants_id = django_filters.ModelMultipleChoiceFilter(
        field_name='participants__id',
        queryset=User.objects.all(),
        to_field_name='id',
        label='User ID',
    )
    participants = django_filters.ModelMultipleChoiceFilter(
        field_name='participants__username',
        queryset=User.objects.all(),
        to_field_name='username',
        label='User username',
    )

    class Meta:
        model = Course
        fields = ['id', 'name']
