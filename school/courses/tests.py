from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase

from users.models import User
from .api.views import CourseViewSet, LessonViewSet
from .factories import CourseFactory, LessonFactory


class TestCaseForCity(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', is_superuser=True)
        self.token = Token.objects.create(user=self.user)
        self.header = {'HTTP_AUTHORIZATION': f'Token {self.token.key}'}

    def test_get_course_without_auth(self):
        response = self.client.get("/api/school/courses/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_course_with_auth(self):
        response = self.client.get("/api/school/courses/", **self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_lesson_without_auth(self):
        response = self.client.get("/api/school/lessons/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_lesson_with_auth(self):
        response = self.client.get("/api/school/lessons/", **self.header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_course_request_factory(self):
        course = CourseFactory(
            name="Test Course",
            duration=1,
            description='wdowkqdiwndu weew',
            category='linux',
        )
        request_factory = APIRequestFactory()
        request = request_factory.get("/api/school/courses/", **self.header)
        course_view = CourseViewSet.as_view({"get": "list"})
        response = course_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_lesson_request_factory(self):
        course = CourseFactory(
            name="Test Course",
            duration=1,
            description='wdowkqdiwndu weew',
            category='linux',
        )
        lesson = LessonFactory(
            name="Test Lesson",
            duration=2,
            description='dadwdcacv',
            course=course,
        )
        request_factory = APIRequestFactory()
        request = request_factory.get("/api/school/lessons/", **self.header)
        lesson_view = LessonViewSet.as_view({"get": "list"})
        response = lesson_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_course(self):
        course = CourseFactory(
            name="Test Course",
            duration=1,
            description='wdowkqdiwndu weew',
            category='linux',
        )
        response = self.client.get("/api/school/courses/", **self.header)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_course_and_lesson(self):
        course = CourseFactory(
            name="Test Course",
            duration=1,
            description='wdowkqdiwndu weew',
            category='linux',
        )
        lesson = LessonFactory(
            name="Test Lesson",
            duration=2,
            description='dadwdcacv',
            course=course,
        )
        response_course = self.client.get("/api/school/courses/", **self.header)
        self.assertEqual(len(response_course.data['results']), 1)
        self.assertEqual(response_course.data['results'][0]['name'], "Test Course")
        self.assertEqual(len(response_course.data['results'][0]['lessons']), 1)
        self.assertEqual(response_course.data['results'][0]['lessons'][0]['name'], "Test Lesson")

        response_lesson = self.client.get("/api/school/lessons/", **self.header)
        self.assertEqual(len(response_lesson.data['results']), 1)
        self.assertEqual(response_lesson.data['results'][0]['name'], "Test Lesson")
        self.assertEqual(len(response_lesson.data['results'][0]['course']), 2)
        self.assertEqual(response_lesson.data['results'][0]['course']['name'], "Test Course")

    def test_create_course_and_lesson(self):
        course = {
            "name": "Test Course",
            "duration": 1,
            "description": "dowkqdiwndu weew",
            "category": "linux"
        }
        response_course = self.client.post("/api/school/courses/", data=course, **self.header)
        self.assertEqual(response_course.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_course.data["name"], "Test Course")
        lesson = {
            "name": "Test Lesson",
            "duration": 2,
            "description": "dadwdcacv",
            "course": response_course.data["id"]
        }
        response_lesson = self.client.post("/api/school/lessons/", data=lesson, format="json", **self.header)
        self.assertEqual(response_lesson.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_lesson.data["name"], "Test Lesson")
