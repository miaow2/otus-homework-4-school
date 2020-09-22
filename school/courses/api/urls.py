from rest_framework import routers

from .views import CourseViewSet, LessonViewSet


class CoursesRootView(routers.APIRootView):

    def get_view_name(self):
        return 'Courses'


router = routers.DefaultRouter()
router.APIRootView = CoursesRootView
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)

app_name = 'courses-api'
urlpatterns = router.urls
