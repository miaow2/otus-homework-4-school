from rest_framework.viewsets import ModelViewSet

from courses import filters
from courses.models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_class = filters.CourseFilterSet


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.select_related('course')
    serializer_class = LessonSerializer
    filterset_class = filters.LessonFilterSet
