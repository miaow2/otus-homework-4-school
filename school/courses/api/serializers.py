from rest_framework import serializers

from courses.models import Course, Lesson
from users.api.nested_serializers import NestedUserSerializer
from .nested_serializers import NestedCourseSerializer, NestedLessonSerializer


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    lessons = NestedLessonSerializer(many=True)
    students = NestedUserSerializer(many=True)
    professors = NestedUserSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            'id', 'name', 'duration', 'text_short', 'lessons', 'students', 'professors'
        ]


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    course = NestedCourseSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'duration', 'text_short', 'course']
