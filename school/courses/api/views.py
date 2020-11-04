from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from courses import filters
from courses.models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_class = filters.CourseFilterSet


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.select_related("course")
    serializer_class = LessonSerializer
    filterset_class = filters.LessonFilterSet


class LeaveCourseAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course = Course.objects.get(id=request.data["course_id"])
        course.participants.remove(user)

        return Response({"status": "ok"}, status=200)
