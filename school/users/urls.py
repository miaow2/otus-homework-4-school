from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


app_name = 'users'
urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('token/', views.TokenCreateView.as_view(), name='create_token'),
]