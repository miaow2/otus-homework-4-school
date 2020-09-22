import django_filters

from .models import Course, Lesson


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
