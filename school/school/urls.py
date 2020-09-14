from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('school/', include('courses.urls')),
]