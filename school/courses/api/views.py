from rest_framework.viewsets import ModelViewSet

from courses.models import Course
from .serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # filterset_class = filters.CourseFilterSet
