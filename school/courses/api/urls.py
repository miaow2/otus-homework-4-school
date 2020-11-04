from django.urls import path
from rest_framework import routers

from .views import CourseViewSet, LeaveCourseAPI, LessonViewSet


class CoursesRootView(routers.APIRootView):
    def get_view_name(self):
        return "Courses"


router = routers.DefaultRouter()
router.APIRootView = CoursesRootView
router.register("courses", CourseViewSet)
router.register("lessons", LessonViewSet)

app_name = "courses-api"
custom_urls = [
    path("courses/leave", LeaveCourseAPI.as_view()),
]
urlpatterns = router.urls + custom_urls
