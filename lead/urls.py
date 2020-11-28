from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Leads API')


urlpatterns = [
    path("", include("apps.urls")),
    path("", schema_view),
]
