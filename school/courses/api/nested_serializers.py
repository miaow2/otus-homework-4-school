from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import ModelSerializer, ValidationError

from courses.models import Course, Lesson

__all__ = [
    'NestedCourseSerializer',
    'NestedLessonSerializer',
]


class NestedCourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name']

    def to_internal_value(self, data):

        if data is None:
            return None

        try:
            return self.Meta.model.objects.get(pk=int(data))
        except ObjectDoesNotExist:
            raise ValidationError(
                "Related object not found using the provided numeric ID: {}".format(pk)
            )



class NestedLessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'name']

