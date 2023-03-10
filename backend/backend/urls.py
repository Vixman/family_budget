from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Family Budget API",
        default_version="v1",
        description="Family budget app api documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth", include("authentication.urls")),
    path("api/income/", include("income.urls")),
    path("api/expenses/", include("expenses.urls")),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
