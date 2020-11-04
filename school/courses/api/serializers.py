from rest_framework import serializers

from courses.models import Course, Lesson
from users.models import User
from users.nested_serializers import NestedUserSerializer
from .nested_serializers import NestedCourseSerializer, NestedLessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons = NestedLessonSerializer(required=False, many=True)
    students = NestedUserSerializer(required=False, many=True)
    professors = NestedUserSerializer(required=False, many=True)
    participants = NestedUserSerializer(required=False, many=True)

    class Meta:
        model = Course
        fields = [
            'id', 'name', 'duration', 'description', 'lessons', 'students', 'professors',
            'participants',
        ]

    def create(self, validated_data):
        print('create')
        participants = validated_data.pop('participants', None)
        instance = super().create(validated_data)

        if participants is not None:
            return self._save_participants(instance, participants)
        return instance

    def update(self, instance, validated_data):
        print(validated_data)
        participants = validated_data.pop('participants', None)

        instance._participants = participants or []

        instance = super().update(instance, validated_data)

        if participants is not None:
            return self._save_participants(instance, participants)
        return instance

    def _save_participants(self, instance, participants):
        if participants:
            instance.participants.set(participants)
        else:
            instance.participants.clear()

        return instance


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    course = NestedCourseSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'duration', 'description', 'course']
