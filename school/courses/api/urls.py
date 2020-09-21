from rest_framework import routers

from .views import CourseViewSet


class CoursesRootView(routers.APIRootView):

    def get_view_name(self):
        return 'Courses'


router = routers.DefaultRouter()
router.APIRootView = CoursesRootView
router.register('courses', CourseViewSet)

app_name = 'courses-api'
urlpatterns = router.urls
