from django.urls import path

from .api import ChangeTokenAPI, LoginAPI, RegisterAPI, UserAPI


app_name = 'users'
urlpatterns = [
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/change-token', ChangeTokenAPI.as_view()),
]
