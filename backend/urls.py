# Imports
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions


# Swagger settings
schema_view = get_schema_view(
    openapi.Info(
        title="Django REST API - On Counter Billing System Backend API",
        default_version="v1",
        description="A Django REST API - On Counter Billing System Backend API",
        contact=openapi.Contact(email="rohit.vilas.ingole@gmail.com"),
        license=openapi.License(name="GPL-3.0 license"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Set the url patters
urlpatterns = [
    path("admin/", admin.site.urls),
    path("jwtauth/", include("backend.apps.jwtauth.urls")),
    path("", include("backend.apps.home.urls")),
    path("employee/", include("backend.apps.employees.urls")),
    path("customer/", include("backend.apps.customers.urls")),
    path("bill/", include("backend.apps.orders.urls")),
    path(
        "swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
