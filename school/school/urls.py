from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from graphene_django.views import GraphQLView
from users.views import LoginView, LogoutView, RegisterView
from .schema import schema
from .views import ContactView, HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('admin/', admin.site.urls),
    path('school/', include('courses.urls')),
    path('api/school/', include('courses.api.urls')),
    path('users/', include('users.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
