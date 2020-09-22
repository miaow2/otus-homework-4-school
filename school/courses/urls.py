from django.urls import path

from . import views


app_name = 'courses'
urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/add/', views.CourseCreateView.as_view(), name='course_add'),
    path('courses/<int:pk>/', views.CourseView.as_view(), name='course'),
    path('courses/<int:pk>/edit/', views.CourseEditView.as_view(), name='course_edit'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('courses/<int:pk>/submit/', views.CourseSubmitView.as_view(), name='course_submit'),

    path('courses/add_lesson/', views.LessonCreateView.as_view(), name='lesson_add'),
    path('lessons/<int:pk>/edit/', views.LessonEditView.as_view(), name='lesson_edit'),
    path('lessons/<int:pk>/delete/', views.LessonDeleteView.as_view(), name='lesson_delete'),
]
