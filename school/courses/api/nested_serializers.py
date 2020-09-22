from rest_framework.serializers import ModelSerializer

from courses.models import Course, Lesson

__all__ = [
    'NestedCourseSerializer',
    'NestedLessonSerializer',
]


class NestedCourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name']


class NestedLessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'name']

