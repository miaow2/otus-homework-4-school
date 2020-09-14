from django.urls import path

from . import views


app_name = 'courses'
urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/add/', views.CourseCreateView.as_view(), name='course_add'),
    path('courses/<int:pk>/', views.CourseView.as_view(), name='course'),
    path('courses/<int:pk>/edit/', views.CourseEditView.as_view(), name='course_edit'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
]
