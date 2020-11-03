from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .api import LoginAPI, RegisterAPI, UserAPI


app_name = 'users'
urlpatterns = [
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
]