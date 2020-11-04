from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from graphene_django.views import GraphQLView
from .api import contacts_view
from .schema import schema


urlpatterns = [
    path("", include("frontend.urls")),
    path("", include("users.urls")),
    path("api/", include("courses.api.urls")),
    path("api/contacts/", contacts_view),
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema), name="graphql"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
