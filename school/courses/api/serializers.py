from rest_framework import serializers

from courses.models import Course, Lesson
from users.nested_serializers import NestedUserSerializer
from .nested_serializers import NestedCourseSerializer, NestedLessonSerializer


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    lessons = NestedLessonSerializer(required=False, many=True)
    students = NestedUserSerializer(required=False, many=True)
    professors = NestedUserSerializer(required=False, many=True)

    class Meta:
        model = Course
        fields = [
            'id', 'name', 'duration', 'description', 'lessons', 'students', 'professors'
        ]


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    course = NestedCourseSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'duration', 'description', 'course']
